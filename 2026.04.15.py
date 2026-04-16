'''
import math as m
print(m.sin(m.pi/2.0))

import random as rd
a=rd.random()
print(a)

import random as rd
a= list(range(1,11))
rd.shuffle(a)
print(a)
'''
'''
import turtle as t
t.setup(width=400, height=400)
for i in range(200):
    t.forward(i)
    t.left(93)
t.done()
'''
'''
while(True):
    try:
#        a, b= input('두 수를 입력하시오:').split()
#        result=int(a)/int(b)
        a,b=map(int,input('두 수를 입력하시오:').split(','))
        print('{}/{}={}'.format(a,b,result))
        break
    except:
        print('수가 정확한지 확인하세요.')
        
'''
'''
str3=input('세개의 숫자를 입력하세요.').split()
istr3=list(map(int,str3))
print(istr3)
'''
'''
a, b, c=map(int, input('세개의 숫자를 입력하시오.:').split()
print(a,b,c)
'''
'''
try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print('오류 : 0으로 나눔을 시도했습니다.')
except ValueError:
    print('오류 : 입력 값이 정수나 실수가 아닙니다.')
except:
    print('오류 : 10 2와 같이 두 정수를 입력하세요.')
else:
    print('{} / {} = {}'.format(a, b, result))

'''

class Cat:
# 생성자 혹은 초기화 메소드라 한다
    def __init__(self, name, color='흰색'):
        self.name = name # name이라는 인스턴스 변수를 생성
        self.color = color # color라는 인스턴스 변수를 생성
# 고양이의 정보를 출력하는 메소드
    def meow(self):
        print('내이름은 {}, 색깔은 {}, 야옹 야옹~~'.format(self.name, self.color))
nabi = Cat('나비', '검정색') # nabi 인스턴스 생성
nero = Cat('네로', '흰색') # nero 인스턴스 생성
mimi = Cat('미미', '갈색') # mini 인스턴스 생성
nabi.meow()
nero.meow()
mimi.meow()
