'''
game_score=int(input('게임점수를 입력하세요:'))
if game_score>1000:
    print('당신은 고수입니다.')
'''
'''
a=int(input('num_a='))
b=int(input('num_b='))
if a==b:
    print('두 값이 일치합니다.')
'''
'''
number=int(input('정수를 입력하세요:'))
print('n=',number)
if number%2==0:
    print(number,'은(는) 짝수입니다')
'''
'''
number=int(input('정수를 입력하세요:'))
print('x=',number)
if number>0:
    print(number,'은(는) 자연수입니다')
'''
'''
game_score=int(input('게임 점수를 입력하세요:'))
if game_score>1000:
    print('고수입니다.')
else:
    print('입문자입니다.')
'''
'''
a=int(input('한 정수를 입력하시오:'))
b=int(input('다른 정수를 입력하시오:'))
if a==b:
    print('두 값이 일치합니다.')
else:
    print('두 값이 일치하지 않습니다.')
      
'''
'''
age=int(input('당신은 성인인가요(성인이면 1, 미성년자면 0):'))
if age==0:
    print('당신은 미성년자입니다.')
if age==1:
    marriage=int(input('결혼을 하셨나요(기혼이면1, 미혼이면0):'))
    if marriage==1:
        print('당신은 결혼한 성인입니다')
    else:
        print('당신은 결혼하지 않은 성인입니다.')
'''
'''
num=2
print(num>=1 and num<=10)
'''
'''
age=int(input('age='))
if age>10 and age<=19:
    print('청소년입니다.')
'''

speed=int(input('자동차의 속도를 입력하세요(단위:km/h):'))
if speed>=100:
    print('고속')
elif speed<60:
    print('저속')
else:
    print('중속')
