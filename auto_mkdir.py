#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:19:05 2020

@author: wangmeiqi
"""
#自動創資料夾

import os 

# your input folder
route = '/Users/wangmeiqi/code_and_data/HCC/ntuh/ct'

# your output folder
save_route = '/Users/wangmeiqi/code_and_data/HCC/ntuh/ct_3d_non_cor'

dir_ = []


for root, dirs, files in os.walk(route):
    
    for dir in dirs:
        
        dir_.append(dir)
        
        print(dir)
        
  
num = len(dir_)


for i in range(num):
    
    path = os.path.join(save_route, dir_[i])
    
    if not os.path.isdir(path):
        
        os.mkdir(path)
        
