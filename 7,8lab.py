'''
from datetime import datetime

now = datetime.now()

h = now.hour

if h < 12:
    ampm = "오전"
    hour_12 = 12 if h == 0 else h
else:
    ampm = "오후"
    hour_12 = 12 if h == 12 else h - 12

print(f"오늘의 날짜: {now.year}년 {now.month}월 {now.day}일")
print(f"현재 시간: {ampm} {hour_12}시 {now.minute}분")
'''
'''
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas - dt.datetime.now()
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format( \
time_gap.days,time_gap.seconds // 3600))
'''
'''
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
a_day=dt.datetime(2036, 1, 1)
time_gap=a_day- dt.datetime.now()
print('2036년 새해까지는{}일 {}시간 남았습니다.'.format(\
    time_gap.days, time_gap.seconds//3600))
'''
'''
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
birthday=dt.datetime(2026, 7, 5)
time_gap=birthday-dt.datetime.now()
print('2026년 생일까지는 {}일 {}시간 남았습니다.'.format(time_gap.days, time_gap.seconds//3600))
'''
'''
from datetime import datetime, timedelta

today = datetime.now()

thousand_days = timedelta(days=1000)

future_date = today + thousand_days

print(f"오늘 날짜: {today.strftime('%Y-%m-%d')}")
print(f"1,000일 후: {future_date.strftime('%Y-%m-%d')}")
'''
'''
from datetime import datetime, timedelta

input_date = input("처음 사귄 연도 월 일을 띄어쓰기로 입력하세요 (예: 2024 1 1): ")

year, month, day = map(int, input_date.split())

start_date = datetime(year, month, day)

hundred_days = start_date + timedelta(days=99)

print("-" * 30)
print(f"사귀기 시작한 날: {start_date.strftime('%Y년 %m월 %d일')}")
print(f"축하합니다! 100일 기념일은 {hundred_days.strftime('%Y년 %m월 %d일')}입니다.")
print("-" * 30)
'''
'''
import random

five_multiples = [random.randrange(0, 101, 5) for _ in range(3)]

print("0에서 100 이하의 정수 중에서 5의 배수")
print(five_multiples)
'''
'''
import random

numbers = range(1, 11)

random_samples = random.sample(numbers, 3)

print(random_samples)
'''

