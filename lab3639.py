'''
for _ in range(5):
    print('Hello, Python!')
for i in range(5):
    print(i)
'''
'''
print(list(range(1, 101)))
print(list(range(1, 101, 2)))
print(list(range(2, 101, 2)))
print(list(range(-100, 0)))
'''
'''
s=0
for i in range(1,101):
    s=s+i
    print('i={}, s={}'.format(i,s))
'''
'''
for i in range(0,101,2):
    print(i)
'''
'''
for i in range(1,101,2):
    print(i)
'''

n=7
for i in range(n,0,-1):
    st=' '
    for j in range(i):
        st=' '+ st
    print(st+'#')
