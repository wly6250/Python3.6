# -*- coding: utf-8 -*-
z=int(input('请输入想要显示的斐波那契数列个数：'))
x=z-2
k=[1,]
a1=0
a2=1
n=0
while n<=x:
    a3=a1+a2
    k.insert(1+n,a3)
    n=n+1
    a1=a2
    a2=a3
print(k)
