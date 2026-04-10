'''
person={'이름':'홍길동', '나이': 26, '몸무게': 82}
print(person['이름'])
print(person['나이'])
print(person['몸무게'])
'''
'''
students={2019001:'이순신',2019002:'김유신',2019003:'강감찬'}
print(students[2019001])
print(students[2019002])
print(students[2019003])
'''
'''
person={'이름':'홍길동', '나이': 26, '몸무게': 82}
person['국적']='대한민국'
print(person.values())
for key in person:
    print('{}:{}'.format(key, person[key]))
'''
'''
tuple1=(1,2,3)
tuple1[0]=1
print(tuple1[0])
'''
'''
def plusminus(a1,a2):
    return a1+a2,a1-a2
output= plusminus(10,2)
output_list=list(output)
print(type(output_list))
'''
'''
a=100
b=200
print('Before swap:', a, b)
a,b=b,a
print('After swap:', a, b)
'''
'''
set1={0,1,2,2,4,5,5}
print(set1)
set2={0,5,2,2,4,1}
print(set2)
'''

set1={1,2,3,4}
set2={2,4,6,7}
#set3=set1|set2
#set3=set1.union(set2)
#set3=set2|set1
#set3=set2.union(set1)

#set3=set1.intersection(set2)
#set3=set1&set2
#set3=set2.intersection(set1)
#set3=set2&set1

#set3=set1-set2
#set3=set1.difference(set2)

#set3=set2-set1
set3=set2.difference(set1)

print(set3)
