# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:40:14 2018

@author: YangGao
"""

import os

os.chdir('K:\\Documents\\Python\\name--test')

print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split('--')
    
    f_title = f_title.strip()
    f_num = f_num.strip().zfill(3)
    
    new_name = f'{f_num}--{f_title}{f_ext}'
    
    os.rename(f,new_name)    
    
    