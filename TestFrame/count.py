# -*- coding: UTF-8 -*-
#用于判断质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % 2 == 0:
            return  False
    return True