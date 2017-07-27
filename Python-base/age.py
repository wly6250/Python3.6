# -*- coding: utf-8 -*-
while True:
    while True:
        age = input('请输入您的年龄（正整数）：')
        if age.isdigit():              #判断age是否为数字（正整数）
            age = int(age)             #取整
            break
        else:
            print('\n您输入的年龄有误，请重新输入.\n')
    if age < 2 and age >= 0:
        print('\n你是婴儿\n')
        break
    elif age < 6 and age >= 2:
        print('\n你是幼儿\n')
        break
    elif age < 12 and age >= 6:
        print('\n你是儿童\n')
        break
    elif age < 18 and age >= 12:
        print('\n你是青少年\n')
        break
    elif age >=18 and age < 25:
        print('\n你是青年\n')
        break
    elif age >=25 and age < 40:
        print('\n你是中年人\n')
        break
    elif age >=40 and age < 60:
        print('\n你是中老年人\n')
        break
    elif age >=60 and age < 100:
        print('\n你是老年人\n')
        break
    elif age >=100 and age < 200:
        print('\n你是百岁老人\n')
        break
    else:
        print('\n你是老妖怪\n')
        break
print('if not <break>,it will be death loop')
