'''
num=100
print('num=',num)
num=200
print('num=',num)
num=300
print('num=',num)
'''
'''
num=0
for i in range(100):
    num += 100
    print('num=',i, num)
'''

age=int(input('나이를 입력하세요:'))
if age<20:
    print('청소년 할인')
elif age>=65:
    print('경로 우대')
