#!/usr/bin/env python
# requires coolbits be set and `$(id) ALL=(ALL) NOPASSWD: /usr/bin/python /home/$(id)/nvidia-oc.py` in /etc/sudoers

from pynvml import *

nvmlInit()

# This sets the GPU to adjust - if this gives you errors or you have multiple GPUs, set to 1 or try other values
myGPU = nvmlDeviceGetHandleByIndex(0)

# The GPU clock offset value should replace "000" in the line below.
nvmlDeviceSetGpcClkVfOffset(myGPU, 000)

# The memory clock offset should be **multiplied by 2** to replace the "000" below
# For example, an offset of 500 means inserting a value of 1000 in the next line
nvmlDeviceSetMemClkVfOffset(myGPU, 0000)

# The power limit can be set below in mW - 216W becomes 216000, etc. Remove the below line if you don't want to adjust power limits.
# nvmlDeviceSetPowerManagementLimit(myGPU, 000000)
