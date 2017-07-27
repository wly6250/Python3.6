# -*- coding: UTF-8 -*-
#函数id()
#This is the address of the object in memory
#for this object during its lifetime

x = 1
y = x
z = 1
print('数值 x 的 id = ',id(x))
print('数值 y 的 id = ',id(y))
print('数值 z 的 id = ',id(z))

print('x = z?:',x==z)
print('x is z?:',x is z)

a = [1]
b = a
c = [1]
print('列表 a 的 id = ',id(a))
print('列表 b 的 id = ',id(b))
print('列表 c 的 id = ',id(c))

print('a = c?:',a==c)
print('a is c?:',a is c)
