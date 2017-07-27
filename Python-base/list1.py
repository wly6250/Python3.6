# -*- coding: utf-8 -*-
r=list(range(100))
for i in range(len(r)-1):
    r.pop(i)
    print('循环条件i:',i)
    print('处理后的list:',r)
