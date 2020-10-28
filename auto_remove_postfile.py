#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 07:37:13 2020

@author: wangmeiqi
"""

#delet post file

import os


#remove
route = '/Volumes/dataBackup/HCC/infer_0831_1650/train'

mask_list = []

for root, dirs, files in os.walk(route):

    for file in files:
        
        if file[:6] == 'post_v':
            
            filename = os.path.join(root, file)
            
            print(filename)
            
            os.remove(filename)
#end


#move
route = '/Users/wangmeiqi/code_and_data/HCC/output/infer_0831_1650/test/Regi_Reso_PC'

mask_list = []

for root, dirs, files in os.walk(route):

    for file in files:
        
        if file[:5] == 'post_':
            
            filename = os.path.join(root, file)
            
            print(filename)
            
            os.remove(filename)
        