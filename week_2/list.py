# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 17:52:26 2016

@author: sam
"""

list1 = [[1,2,['My']],5,"self",["Samim"]]
list2 = [[1,2,['My']],5,"self",["Samim"]]

list3 = list2

print(list1 == list2)
print(list1 is list2)
print(list3 is list2)
print(list3 is list1)
print(list1 == list3)

print((list1[0][2][:]))
