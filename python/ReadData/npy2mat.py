#!/usr/bin/env python
#
#**#
#Author:		erbiaoger
#Email:			[643747954@qq.com](mailto:643747954@qq.com)
#Date:			2022-10-04
#FileName:		npy2mat.py
#Description:	The purpose of the script is
#Copyright(C):	2022 All rights reserved
#**#
#
import numpy as np
import scipy.io as io

data = np.load('name.npy')
io.savemat('name',{"data": data})
