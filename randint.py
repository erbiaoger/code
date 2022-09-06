#!/usr/bin/env python                                                                                                      1 #
#******************************************#
#Author:        erbiaoger
#Email:         643747954@qq.com
#Date:          2022-06-09
#FileName:      ramdint.py
#Description:   The purpose of the script is
#Copyright(C):  2022 All rights reserved
#******************************************#
#

import numpy as np

n = int(input())

x = []

# n个随机数列表
for i in range(0, n):
    x.append(np.random.randint(1, n))
#print(x)

# 偶数列表
even = [i for i in x if i%2 == 0]
# 奇数列表
odd = [i for i in x if i%2 == 1]

#print(even)
#print(odd)

# 偶数平均数
ave_even = np.mean(even)
# 俩位小数
print(round(ave_even, 2))
# 奇数平均数
ave_odd = np.mean(odd)
print(round(ave_odd, 2))
