#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Create Time: 2016/11/30 16:19:33
# Create author: XiaoFengfeng

"""
生成质数，判断质数
"""

import xutils


def miller_rabin_primality_testing(n, k):
    """
    Miller–Rabin primality test:"https://en.wikipedia.org/wiki/Miller–Rabin primality test"
    """
    if n < 2:
        return False

    d = n - 1
    r = 0

    while not (d & 1):
        r += 1
        d >>= 1

    for _ in range(k):
        a = xutils.randint(n - 4) + 2

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


def isprime(num):
    """
    判断一个数是否是质数
    >>> isprime(97)
    True
    >>> isprime(100)
    False
    """
    if num < 10:
        return num in [2, 3, 5, 7]

    if not (1 & num):
        return False

    return miller_rabin_primality_testing(num, 7)


def getprime(xbits):
    """
    生成一个质数
    >>> getprime(64)
    13505411656529702771
    >>> getprime(64)
    11419939612564061833
    """
    assert xbits > 3

    while True:
        xint = xutils.get_random_odd_int(xbits)
        if isprime(xint):
            return xint


if __name__ == '__main__':
    print(getprime(128))
