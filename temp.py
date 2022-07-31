# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list = [1,2,3,4,5,6,7,8,9,10]
a = {}

a[1] ='ali'

a[2] = 'mamad'

a[3] = 'abed'

b = {}

b[1] ='aaa'

b[2] = 'bbb'

b[3] = 'ccc'

print ('list=', list)

print ('a=' ,a)

print ('b=' ,b)

for x in list :
    if x <= 5:
        a.setdefault(a.__len__()+1,x)
    else :
        b.setdefault(b.__len__()+1,x)
       
print(a)
print(b)


