import torch
import torch.nn.functional as F
from torch.autograd import Variable


# First define all the layers.

class conv_bn(torch.nn.Module):
    def __init__(self, inp_ch, outp_ch):
        super(conv_bn, self).__init__()
        self.conv = torch.nn.Sequential(
                torch.nn.Conv2d(inp_ch, outp_ch, 3),
                torch.nn.BatchNorm2d(outp_ch),
                torch.nn.ReLU(inplace=True)
            )

    def forward(self, x):
        return self.conv(x)


# Then define all the models.

class Model1(torch.nn.Module):
    def __init__(self, in_ch):
        super(Model1, self).__init__()
        self.conv1 = conv_bn(in_ch, 5)
        self.layer = torch.nn.Linear(50 * 50 * 5, 10)

    def forward(self, x):
        x = self.conv1(x)
        return self.layer(x)

# ...