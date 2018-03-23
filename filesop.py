# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 09:53:44 2018

@author: YangGao
"""

with open('AxeheadLundgren.jpg','rb') as rf:
    with open('AxeheardLundgren_copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
