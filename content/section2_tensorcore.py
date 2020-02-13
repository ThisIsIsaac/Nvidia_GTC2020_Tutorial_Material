import tensorflow as tf
from tensorflow import nn as nn
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# diltion, padding, and stride are not accounted for!
# They are assumed to be default values
def get_conv2d_MNK(in_tensor, filter, layout):
    if layout == "NHWC":
        batch_size, in_height, in_width, in_channels = in_tensor.shape

    if layout == "NCHW":
        batch_size, in_channels, in_height, in_width = in_tensor.shape

    filter_height, filter_width, in_channels, out_channels = filter.shape

    out_height = in_height - (filter_height - 1)
    out_width = in_width - (filter_width - 1)

    M = batch_size * out_height * out_width
    N = out_channels
    K = in_channels * filter_width * filter_height

    return (M, N, K)


def approximate_gflops(in_tensor, filters, layout, time):
    if time <= 0:
        raise ValueError("time must be greater than 0")
    M, N, K = get_conv2d_MNK(in_tensor, filters, layout)
    flop = 2*M*N*K
    flops = flop / time
    gflops = flops / 1000000000
    return gflops


### DO NOT CHANGE THESE VALUES ###
batch_size = 8
in_height = 64
in_width = 64
filter_height = 3
filter_width = 3

### CHANGE HERE! ###
in_channels = 19
out_channels = 131
layout = "NCHW"
in_tensor = tf.random.uniform([batch_size, in_channels, in_height, in_width], dtype=tf.dtypes.float16)
filters = tf.random.uniform([filter_height, filter_width, in_channels, out_channels], dtype=tf.dtypes.float16)

### DO NOT CHANGE BELOW ###
# Warming up
%timeit -q nn.conv2d(in_tensor, filters, 1, "VALID", data_format=layout)

# Profile!
elapsed_time = %timeit -o -q nn.conv2d(in_tensor, filters, 1, "VALID", data_format=layout)
print("out_channels %d: %f GFLOPS" % (out_channels, approximate_gflops(in_tensor, filters, layout, elapsed_time.average)))
