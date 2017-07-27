# -*- coding: utf-8 -*-
# 从0到99的100个数中，删除所有的偶数！
r=list(range(100))
for i in range(len(r)//2):
    r.pop(i)
    print('循环条件i:',i)
    print('处理后的list:',r)
