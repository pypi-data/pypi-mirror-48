'''Original code from torchvision:
https://github.com/pytorch/vision/blob/master/torchvision/models/inception.py
licensed under BSD-3
'''
# pylint: disable=arguments-differ
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils import model_zoo
from torchvision.models.inception import BasicConv2d, InceptionA, InceptionB, InceptionC

__all__ = [
    'Inception3S',
    'Inception3XS',
    'inception_v3_s',
    'inception_v3_xs',
    'inception_v3_s_plus',
    'inception_v3_s_wrap',
]

model_urls = {
    'inception_v3_s': 'https://eye2you.org/models/inception_v3_s_eye2you-2bea754f.pth',
    'inception_v3_xs': 'https://eye2you.org/models/inception_v3_xs_eye2you-3a70c6bb.pth'
}


def inception_v3_s(pretrained=False, **kwargs):
    if pretrained:
        if 'transform_input' not in kwargs:
            kwargs['transform_input'] = False
        model = Inception3S(**kwargs)
        model.load_state_dict(model_zoo.load_url(model_urls['inception_v3_s']))
        return model

    return Inception3S(**kwargs)


def inception_v3_xs(pretrained=False, **kwargs):
    if pretrained:
        if 'transform_input' not in kwargs:
            kwargs['transform_input'] = False
        model = Inception3XS(**kwargs)
        model.load_state_dict(model_zoo.load_url(model_urls['inception_v3_xs']))
        return model

    return Inception3XS(**kwargs)


def inception_v3_s_plus(pretrained=False, **kwargs):
    if pretrained:
        if 'transform_input' not in kwargs:
            kwargs['transform_input'] = True
        model = Inception3SPlus(**kwargs)
        model.load_state_dict(model_zoo.load_url(model_urls['inception_v3_s']), strict=False)
        return model

    return Inception3SPlus(**kwargs)


def inception_v3_s_wrap(pretrained=False, **kwargs):

    return Inception3SWrap(**kwargs)


class Inception3S(nn.Module):

    def __init__(self, num_classes=1000, aux_logits=True, transform_input=False, in_channels=3):
        super(Inception3S, self).__init__()
        self.aux_logits = aux_logits
        self.transform_input = transform_input
        self.Conv2d_1a_3x3 = BasicConv2d(in_channels, 32, kernel_size=3, stride=2)
        self.Conv2d_2a_3x3 = BasicConv2d(32, 32, kernel_size=3)
        self.Conv2d_2b_3x3 = BasicConv2d(32, 64, kernel_size=3, padding=1)
        self.Conv2d_3b_1x1 = BasicConv2d(64, 80, kernel_size=1)
        self.Conv2d_4a_3x3 = BasicConv2d(80, 192, kernel_size=3)
        self.Mixed_5b = InceptionA(192, pool_features=32)
        self.Mixed_5c = InceptionA(256, pool_features=64)
        self.Mixed_5d = InceptionA(288, pool_features=64)
        self.Mixed_6a = InceptionB(288)
        if aux_logits:
            self.AuxLogits = InceptionAux(288, num_classes)
        self.Mixed_6b = InceptionC(768, channels_7x7=128)
        self.Mixed_6c = InceptionC(768, channels_7x7=160)
        self.Mixed_6d = InceptionC(768, channels_7x7=160)
        self.Mixed_6e = InceptionC(768, channels_7x7=192)
        self.fc = nn.Linear(768, num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):
                import scipy.stats as stats
                stddev = m.stddev if hasattr(m, 'stddev') else 0.1
                X = stats.truncnorm(-2, 2, scale=stddev)
                values = torch.Tensor(X.rvs(m.weight.numel()))
                values = values.view(m.weight.size())
                m.weight.data.copy_(values)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, x, mask=None, segment=None):
        #if self.transform_input:
        #    x_ch0 = torch.unsqueeze(x[:, 0], 1) * (0.229 / 0.5) + (0.485 - 0.5) / 0.5
        #    x_ch1 = torch.unsqueeze(x[:, 1], 1) * (0.224 / 0.5) + (0.456 - 0.5) / 0.5
        #    x_ch2 = torch.unsqueeze(x[:, 2], 1) * (0.225 / 0.5) + (0.406 - 0.5) / 0.5
        #    x = torch.cat((x_ch0, x_ch1, x_ch2), 1)
        # 299 x 299 x 3
        x = self.Conv2d_1a_3x3(x)
        # 149 x 149 x 32
        x = self.Conv2d_2a_3x3(x)
        # 147 x 147 x 32
        x = self.Conv2d_2b_3x3(x)
        # 147 x 147 x 64
        x = F.max_pool2d(x, kernel_size=3, stride=2)
        # 73 x 73 x 64
        x = self.Conv2d_3b_1x1(x)
        # 73 x 73 x 80
        x = self.Conv2d_4a_3x3(x)
        # 71 x 71 x 192
        x = F.max_pool2d(x, kernel_size=3, stride=2)
        # 35 x 35 x 192
        x = self.Mixed_5b(x)
        # 35 x 35 x 256
        x = self.Mixed_5c(x)
        # 35 x 35 x 288
        x = self.Mixed_5d(x)
        # 35 x 35 x 288
        if self.training and self.aux_logits:
            aux = self.AuxLogits(x)
        # 35 x 35 x 288
        x = self.Mixed_6a(x)
        # 17 x 17 x 768
        x = self.Mixed_6b(x)
        # 17 x 17 x 768
        x = self.Mixed_6c(x)
        # 17 x 17 x 768
        x = self.Mixed_6d(x)
        # 17 x 17 x 768
        x = self.Mixed_6e(x)
        # 17 x 17 x 768
        #x = F.avg_pool2d(x, kernel_size=17)
        x = F.adaptive_avg_pool2d(x, (1, 1))
        # 1 x 1 x 2048
        x = F.dropout(x, training=self.training)
        # 1 x 1 x 2048
        x = x.view(x.size(0), -1)
        # 2048
        x = self.fc(x)
        # 1000 (num_classes)
        if self.training and self.aux_logits:
            return x, aux
        return x


class Inception3SWrap(Inception3S):

    def forward(self, x, mask=None, segment=None):
        x = torch.cat((x, segment), dim=1)
        if mask is not None:
            x = x * mask
        return super().forward(x)


class Inception3XS(nn.Module):

    def __init__(self, num_classes=1000, transform_input=False, in_channels=3):
        super(Inception3XS, self).__init__()
        self.transform_input = transform_input
        self.Conv2d_1a_3x3 = BasicConv2d(in_channels, 32, kernel_size=3, stride=2)
        self.Conv2d_2a_3x3 = BasicConv2d(32, 32, kernel_size=3)
        self.Conv2d_2b_3x3 = BasicConv2d(32, 64, kernel_size=3, padding=1)
        self.Conv2d_3b_1x1 = BasicConv2d(64, 80, kernel_size=1)
        self.Conv2d_4a_3x3 = BasicConv2d(80, 192, kernel_size=3)
        self.Mixed_5b = InceptionA(192, pool_features=32)
        self.Mixed_5c = InceptionA(256, pool_features=64)
        self.Mixed_5d = InceptionA(288, pool_features=64)
        self.fc = nn.Linear(288, num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):
                import scipy.stats as stats
                stddev = m.stddev if hasattr(m, 'stddev') else 0.1
                X = stats.truncnorm(-2, 2, scale=stddev)
                values = torch.Tensor(X.rvs(m.weight.numel()))
                values = values.view(m.weight.size())
                m.weight.data.copy_(values)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, x, mask=None, segment=None):
        # if self.transform_input:
        #     x_ch0 = torch.unsqueeze(x[:, 0], 1) * (0.229 / 0.5) + (0.485 - 0.5) / 0.5
        #     x_ch1 = torch.unsqueeze(x[:, 1], 1) * (0.224 / 0.5) + (0.456 - 0.5) / 0.5
        #     x_ch2 = torch.unsqueeze(x[:, 2], 1) * (0.225 / 0.5) + (0.406 - 0.5) / 0.5
        #     x = torch.cat((x_ch0, x_ch1, x_ch2), 1)
        # 299 x 299 x 3
        x = self.Conv2d_1a_3x3(x)
        # 149 x 149 x 32
        x = self.Conv2d_2a_3x3(x)
        # 147 x 147 x 32
        x = self.Conv2d_2b_3x3(x)
        # 147 x 147 x 64
        x = F.max_pool2d(x, kernel_size=3, stride=2)
        # 73 x 73 x 64
        x = self.Conv2d_3b_1x1(x)
        # 73 x 73 x 80
        x = self.Conv2d_4a_3x3(x)
        # 71 x 71 x 192
        x = F.max_pool2d(x, kernel_size=3, stride=2)
        # 35 x 35 x 192
        x = self.Mixed_5b(x)
        # 35 x 35 x 256
        x = self.Mixed_5c(x)
        # 35 x 35 x 288
        x = self.Mixed_5d(x)
        # 35 x 35 x 288
        x = F.avg_pool2d(x, kernel_size=35)
        # 1 x 1 x 2048
        x = F.dropout(x, training=self.training)
        # 1 x 1 x 2048
        x = x.view(x.size(0), -1)
        # 2048
        x = self.fc(x)
        # 1000 (num_classes)
        return x


class InceptionAux(nn.Module):

    def __init__(self, in_channels, num_classes):
        super(InceptionAux, self).__init__()
        self.conv0 = BasicConv2d(in_channels, 128, kernel_size=1)
        self.conv1 = BasicConv2d(128, 768, kernel_size=5)
        self.conv1.stddev = 0.01
        self.fc = nn.Linear(768, num_classes)
        self.fc.stddev = 0.001

    def forward(self, x):
        # 17 x 17 x 768
        x = F.avg_pool2d(x, kernel_size=7, stride=7)
        x = F.adaptive_avg_pool2d(x, (5, 5))
        # 5 x 5 x 768
        x = self.conv0(x)
        # 5 x 5 x 128
        x = self.conv1(x)
        # 1 x 1 x 768
        x = x.view(x.size(0), -1)
        # 768
        x = self.fc(x)
        # 1000
        return x


class Inception3SPlus(nn.Module):

    def __init__(self, num_classes=1000, aux_logits=True, transform_input=False, in_channels=3):
        super().__init__()
        self.aux_logits = aux_logits
        self.transform_input = transform_input
        self.Conv2d_1a_3x3 = BasicConv2d(in_channels, 32, kernel_size=3, stride=2)
        self.Conv2d_2a_3x3 = BasicConv2d(32, 32, kernel_size=3)
        self.Conv2d_2b_3x3 = BasicConv2d(32, 64, kernel_size=3, padding=1)
        self.Conv2d_3b_1x1 = BasicConv2d(64, 80, kernel_size=1)
        self.Conv2d_4a_3x3 = BasicConv2d(80, 192, kernel_size=3)
        self.Mixed_5b = InceptionA(192, pool_features=32)
        self.Mixed_5c = InceptionA(256, pool_features=64)
        self.Mixed_5d = InceptionA(288, pool_features=64)
        self.Mixed_6a = InceptionB(288)
        if aux_logits:
            self.AuxLogits = InceptionAux(288, num_classes)
        self.Mixed_6b = InceptionC(768, channels_7x7=128)
        self.Mixed_6c = InceptionC(768, channels_7x7=160)
        self.Mixed_6d = InceptionC(768, channels_7x7=160)
        self.Mixed_6e = InceptionC(768, channels_7x7=192)
        self.Vessel_Preconv = nn.Conv2d(1, 768, 1, bias=False)
        self.VesselMultiplier = nn.Conv2d(in_channels=1, out_channels=768, kernel_size=1, bias=False)
        self.VesselMultiplier.weight.data.copy_(torch.ones((768, 1, 1, 1)))
        self.VesselMultiplier.weight.requires_grad = False
        self.Vessel = BasicConv3d(768, 768, kernel_size=(2, 3, 3), padding=(0, 1, 1))
        self.fc = nn.Linear(768, num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):
                import scipy.stats as stats
                stddev = m.stddev if hasattr(m, 'stddev') else 0.1
                X = stats.truncnorm(-2, 2, scale=stddev)
                values = torch.Tensor(X.rvs(m.weight.numel()))
                values = values.view(m.weight.size())
                m.weight.data.copy_(values)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

        m = self.Vessel_Preconv
        values = torch.ones(m.weight.numel())
        values = values.view(m.weight.size())
        m.weight.data.copy_(values)
        for p in m.parameters():
            p.requires_grad = False

    def forward(self, x, segmentation, *args):
        #if self.transform_input:
        #    x_ch0 = torch.unsqueeze(x[:, 0], 1) * (0.229 / 0.5) + (0.485 - 0.5) / 0.5
        #    x_ch1 = torch.unsqueeze(x[:, 1], 1) * (0.224 / 0.5) + (0.456 - 0.5) / 0.5
        #    x_ch2 = torch.unsqueeze(x[:, 2], 1) * (0.225 / 0.5) + (0.406 - 0.5) / 0.5
        #    x = torch.cat((x_ch0, x_ch1, x_ch2), 1)
        #x = torch.cat((x, mask), dim=1)
        #print(x.shape)
        # 299 x 299 x 3
        x = self.Conv2d_1a_3x3(x)
        #print(x.shape)
        # 149 x 149 x 32
        x = self.Conv2d_2a_3x3(x)
        #print(x.shape)
        # 147 x 147 x 32
        x = self.Conv2d_2b_3x3(x)
        #print(x.shape)
        # 147 x 147 x 64
        x = F.max_pool2d(x, kernel_size=3, stride=2)
        #print(x.shape)
        # 73 x 73 x 64
        x = self.Conv2d_3b_1x1(x)
        #print(x.shape)
        # 73 x 73 x 80
        x = self.Conv2d_4a_3x3(x)
        #print(x.shape)
        # 71 x 71 x 192
        x = F.max_pool2d(x, kernel_size=3, stride=2)
        #print(x.shape)
        # 35 x 35 x 192
        x = self.Mixed_5b(x)
        #print(x.shape)
        # 35 x 35 x 256
        x = self.Mixed_5c(x)
        #print(x.shape)
        # 35 x 35 x 288
        x = self.Mixed_5d(x)
        #print(x.shape)
        # 35 x 35 x 288
        if self.training and self.aux_logits:
            aux = self.AuxLogits(x)
        # 35 x 35 x 288
        x = self.Mixed_6a(x)
        #print(x.shape)
        # 17 x 17 x 768
        x = self.Mixed_6b(x)
        #print(x.shape)
        # 17 x 17 x 768
        x = self.Mixed_6c(x)
        #print(x.shape)
        # 17 x 17 x 768
        x = self.Mixed_6d(x)
        #print(x.shape)
        # 17 x 17 x 768
        x = self.Mixed_6e(x)
        #print(x.shape, mask.shape)
        # 17 x 17 x 768
        segmentation = F.adaptive_avg_pool2d(segmentation, (x.shape[2:]))
        #print(x.shape, mask.shape)
        device = 'cpu' if not x.is_cuda else x.get_device()
        segmentation = F.conv2d(segmentation, torch.ones((768, 1, 1, 1), device=device))
        #mask = F.conv2d(mask, self.vessel_projection)
        x = torch.stack((x, segmentation), dim=2)
        #print(x.shape)
        x = self.Vessel(x)
        #print(x.shape)
        x = F.adaptive_avg_pool2d(x.squeeze(dim=2), (1, 1))
        #print(x.shape)
        # 1 x 1 x 2048
        x = F.dropout(x, training=self.training)
        #print(x.shape)
        # 1 x 1 x 2048
        x = x.view(x.size(0), -1)
        #print(x.shape, 'mm')
        # 2048
        x = self.fc(x)
        #print(x.shape)
        # 1000 (num_classes)
        if self.training and self.aux_logits:
            return x, aux
        return x


class BasicConv3d(nn.Module):

    def __init__(self, in_channels, out_channels, **kwargs):
        super().__init__()
        self.conv = nn.Conv3d(in_channels, out_channels, bias=False, **kwargs)
        self.bn = nn.BatchNorm3d(out_channels, eps=0.001)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return F.relu(x, inplace=True)
