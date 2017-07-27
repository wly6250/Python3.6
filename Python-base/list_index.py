names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
print('All name list:',names)
name1=input('Please input your name:')
if name1 in names:
    print('Your score is:%s' %scores[names.index(name1)])
else:
    print('Can\'t find your score!')
