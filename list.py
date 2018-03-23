# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 16:14:10 2018

@author: YangGao
"""

courses = ['History', 'Math', 'CompSci','Physics','English']
 


for index,course in enumerate(courses,start =1):
    print(index,course)

courses_str = '-'.join(courses)

new_list = courses_str.split('-')
print(new_list)

cs_courses = {'Math', 'History', 'Physics','CompSci'}
art_courses = {'Math', 'History', 'Art', 'Design'}

print(cs_courses.union(art_courses))





