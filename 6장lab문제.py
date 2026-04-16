'''
capital_dic={'Korea':'Seoul','China':'Beijing','USA':'Washington DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])

fruits_dic={'apple':5000,'banana':4000,'grape':5300,'melon':6500}
for fruit, price in fruits_dic.items():
    print('{}의 가격은 {}입니다.'.format(fruit, price))
'''
'''
person={'이름':'홍길동','나이':26,'몸무게':82}
person['특징']='분신술'
person['아버지']='홍판서'
del person['나이']
print(person)
'''
'''
capital_dic={'Korea':'Seoul','China':'Beijing','USA':'Washington DC'}
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)
'''

fruits_dic={'apple':6000,'melon':3000,'banana':5000,'orange':7000}
print(fruits_dic.keys())
print(fruits_dic.values())

fruits_dic.pop('apple',6000)
print(fruits_dic)

fruits_dic.clear()
print(fruits_dic)
