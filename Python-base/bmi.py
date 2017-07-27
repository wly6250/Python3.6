# -*- coding: utf-8 -*-
print('<Body Mass Index Test>')
a=input('please enter your hight(m):')
b=input('please enter your weight(Kg):')
print('your hight=',a,'(m)')
print('your weight=',b,'(Kg)')
bmi=float(b)/float(a)/float(a)
print('Yours BMI= %.1f' %(bmi))
if bmi<18.5:
    print('偏瘦')
elif 18.5<=bmi<24:
    print('正常')
elif 24<=bmi<27:
    print('超重')
elif 27<=bmi<32:
    print('肥胖')
else:
    print('极度肥胖')
