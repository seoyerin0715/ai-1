'''
even_list=[2,4,6,8,10]
print(even_list)
'''
'''
even_list=list(range(2,11,2))
print(even_list)
'''
'''
nations=['Korea','China','India','Nepal']
print('nations=',nations)
'''
'''
friends = ['길동', '철수', '은지', '지은', '영민']
print('firends=',friends)
'''
'''
string = ['X', 'Y', 'Z']
print('string=',string)
'''
'''
prime_list=[2,3,5,7]
print('prime_list의 첫 원소:',prime_list[0])
print('prime_list의 마지막 원소:',prime_list[3])
print('prime_list의 마지막 원소:',prime_list[-1])
'''
'''
nations=['Korea','China','Russia','Malaysia']
print('nations의 첫 원소',nations[0])
print('nations의 마지막 원소:',nations[-1])
'''
'''
prime_list = [2, 3, 5, 7]
print("소수 목록 :", prime_list)
prime_list.append(11)
print("추가 후 소수 목록 :", prime_list)

prime_list = [2, 3, 5, 7, 11]
print("삭제 전 소수 목록 :", prime_list)

prime_list.remove(3)
print("삭제 후 소수 목록 :", prime_list)
'''
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가목록:',nations)
nations.append('Nepal')
print('추가 후 국가목록:',nations)
targets = ['Japan', 'Russia']

for nation in targets:
    if nation in nations:
        print(f"{nation} 는(은) 국가 목록에 있습니다.")
    else:
        print(f"{nation} 는(은) 국가 목록에 없습니다.")

