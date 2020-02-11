# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:41:04 2020

@author: Administrator
"""

x=input("體重")
y=input("身高")
x=float(x)
y=float(y)
z=float(x//y**2)
print('您的BMI值是:',z)
if z<18.5:
    print('體重過輕!')
elif z<24:
    print('體重正常!')
else :
    print('體重過重!')