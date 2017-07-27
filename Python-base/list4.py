# -*- coding: utf-8 -*-
r=list(range(100))
x=0
for i in r:
    r.pop(i)
    x=x+1
    print('循环条件i:',i)
    print('循环次数:',x)
    print('处理后list长:',len(r))
    print('处理后的list:',r)


