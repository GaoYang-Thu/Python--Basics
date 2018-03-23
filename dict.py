# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:32:30 2018

@author: YangGao
"""

student = {'name':'John', 'age':25, 'courses':['Math','CompSci']}

print(student.items())
#del student['age']
#student.update({'name':'Jane','age':28,'phone':'666-6666'})

#print(student.get('non', 'Not Found'))
for key, value in student.items():
    print(key,value)
