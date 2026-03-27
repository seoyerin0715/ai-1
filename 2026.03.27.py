'''
for i in range(-2,-10,-2):
    print(i,end=' ')

'''
'''
s=0
for i in range(1,11):
    s=s+i
    print('i={},s={}'.format(i,s))
print('1에서 10까지의 합:',s)

'''
'''
n=int(input('합계를 구할 수를 입력하세요:'))
s=0
for i in range(0,n):
    s=s+(i+1)
print('1부터 {}까지의 합은 {}' .format(n,s))

'''
'''
n=int(input('수를 입력하세요:'))
fact=1
for i in range(1,n+1):
    fact=fact*i
print('{}!={}'.format(n,fact))
'''
'''
summer_fruits=['수박','참외','체리','포도']
for fruit in summer_fruits:
    print(fruit, end=' ')
'''
'''
for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={:2d}'.format(i,j,i*j),end=' ')
    print()
'''
'''
n=7
for i in range(n):
    st=''
    for j in range(i):
        st=st+' '
    print(st+'#')


n=7
for i in range(n):
    print(' '*i+'#')

'''

n=int(input('수를 입력하세요:'))
is_prime=True
for num in range(2,n):
    if n % num == 0:
        is_prime = False
print(n,'is prime:',is_prime)



