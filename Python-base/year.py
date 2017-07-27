# -*- coding: utf-8 -*-
name = input('please input your name:')
print('hello',name,'let us count your years old')
while True:
    a = input('your year of birth is:')
    if a.isdigit():              #判断age是否为数字（正整数）
        b = 2017 - int(a)
        print(name,'is',b,'years old now!')
        if int(a) < 2000:
            print('00 before')
        else:
            print('00 after')
        break
    else:
        print('your input is error,please enter again')
