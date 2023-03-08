#!/usr/bin/env python
#
#**#
#Author:		erbiaoger
#Email:			[643747954@qq.com](mailto:643747954@qq.com)
#Date:			2022-10-04
#FileName:		mseed2h5.py
#Description:	The purpose of the script is
#Copyright(C):	2022 All rights reserved
#**#
#
import h5py
import numpy as np
from obspy import read
import re
import os
import scipy.io as io


file_dir = "/users/erbiaoger/DAS/osfstorage-archive"
for root, dirs, files in os.walk(file_dir, topdown=False):
    # print(root)     # 当前目录路径
    # print(dirs)     # 当前目录下所有子目录
    # print(files)        # 当前路径下所有非目录子文件
    for file_name in files:
        
        if ".mseed" in file_name:
        
            write_name = file_name.replace(".mseed", ".h5") 
            #print(write_name)
            st = read(file_name)
    
            a = st.__str__(extended=True)
            size = re.search("[0-9]*", a) # 寻找size大小
            raw = int(size.group(0)) # 
            column = st[0].data.size
            """
            st:
                some information...
                
                data:
                    [[...]
                     ...
                     ...
                     [...]]
                     
                     
            """

    
            data1 = np.ones((raw, column))
                

            
            for i in range(raw):
                data1[i] = st[i].data
            

            #print(data1)
            with h5py.File(write_name, 'w') as f:            
                f.create_dataset("mydataset", data=data1)
    
            #print(write_name)
            #print(data1.shape)
        
    






