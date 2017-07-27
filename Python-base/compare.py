# -*- coding: utf-8 -*-
print('どちらが最大値でしょうか')
a = int(input('please enter the first number:'))
b = int(input('please enter the second number:'))
c = int(input('please enter the third number:'))
if a < b:
    max = b
else:
    max = a
if max < c:
    max = c
print('以上の数値の中に最大値は：',max)
