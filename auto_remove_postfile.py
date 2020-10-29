#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 07:37:13 2020

@author: wangmeiqi
"""

#delet post file

import os


#remove
#set parameters from here
route = '/Volumes/dataBackup/HCC/infer_0831_1650/train'

text = 'post_v'

text_num = 5

#########################################################################################

mask_list = []

for root, dirs, files in os.walk(route):

    for file in files:
        
        if file[:text_num + 1] == text:
            
            filename = os.path.join(root, file)
            
            print(filename)
            
            os.remove(filename)
#end


#move
#set parameters from here
route = '/Users/wangmeiqi/code_and_data/HCC/output/infer_0831_1650/test/Regi_Reso_PC'

text = 'post_'

text_num = 4

#########################################################################################

mask_list = []

for root, dirs, files in os.walk(route):

    for file in files:
        
        if file[:text_num + 1] == text:
            
            filename = os.path.join(root, file)
            
            print(filename)
            
            os.remove(filename)
        
