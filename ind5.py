#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_arg(*args):
    if args:
        k = 0
        els = 0
        c = 0
        for arg in args:
            if arg < 0:
                k += 1
            elif arg < 0:
                c = args
                break
            elif 0 < k < 2:
                els += arg
        return els - c
    else:
        return None


if __name__ == '__main__':
    print(sum_arg(-5, 2, 4, -5, 9, -5))
    print(sum_arg())
