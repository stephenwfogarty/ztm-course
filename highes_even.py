#!/usr/bin/env python


def higest_even(li):
    even = [n for n in li if n % 2 == 0]
    print(max(even))

higest_even([2,10,2,3,4,8,11])