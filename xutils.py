#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Create Time: 2016/12/02 11:12:22
# Create author: XiaoFengfeng

import os
import binascii
from struct import pack


def get_random_int(xbits):
    xbytes, ybits = divmod(xbits, 8)
    rbyte = os.urandom(xbytes)
    if ybits > 0:
        rvalue = ord(os.urandom(1))
        rvalue >>= (8 - ybits)
        rbyte = pack("B", rvalue) + rbyte

    value = int(binascii.hexlify(rbyte), 16)

    value |= 1 << (xbits - 1)

    return value


def get_random_odd_int(xbits):
    value = get_random_int(xbits)

    return value | 1


def randint(maxvalue):
    bitsize = len(bin(maxvalue)) - 2

    x = 0
    while True:
        xint = get_random_int(bitsize)
        if xint <= maxvalue:
            break

        if x and x % 10 == 0:
            bitsize -= 1
        x += 1

    return xint
