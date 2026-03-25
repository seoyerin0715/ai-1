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
'''
age=int(input('나이를 입력하세요:'))
if age<20:
    print('청소년 할인')
elif age>=65:
    print('경로 우대')
'''
'''
time=int(input('시간을 입력하세요:'))
if time<12:
    print('오전입니다')
else:
    print('오후입니다')

'''

num=int(input('숫자를 입력하세요:'))

if num<0:
    print(num,'은 음수입니다.')
elif num%2==0:
    print(num,'은 짝수입니다.')
else :
    print(num,'은 홀수입니다.')
