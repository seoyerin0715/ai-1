'''
isum=0
n_list=[0,2,5,10]
for i in n_list:
    isum += i
print(isum)
'''
'''
n_list=[0,2,5,10]
isum=0
i=0
while i<len(n_list):
    isum += n_list[i]
    i += 1

print(isum)
'''
'''
selected= None
while selected not in ['가위','바위','보']:
    selected=input('가위, 바위, 보 중에서 선택하세요>')
print('선택한 값은:', selected)
'''
'''
st='Programing'
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)
print('The end')
'''
'''
def iplus(x1, x2):
    isum=x1+x2
    return isum
hap=iplus(4,5)
print(hap)
'''
'''
def print_star():
    print('*************')
a=print_star()
print(a)
'''
'''
def root(a,b,c):
    x1=(-b+(b**2.0 -4.0*a*c)**0.5)/(2.0*a)
    x2=(-b-(b**2.0 -4.0*a*c)**0.5)/(2.0*a)
    return x1,x2
r1,r2=root(1,2,3)
print(r1,r2)
'''
'''
def root(a,b,c):
    if b**2.0 -4.0*a*c<0:
        return None,None
    else:
        x1=(-b+(b**c)**0.5)/(2.0*a)
        x2=(-b-(b**2.0 -4.0*a*c)**0.5)/(2.0*a)
        return x1,x2
r1,r2=root(1,2,3)
print(r1,r2)
'''
'''
def root(a,b,c):
    if b**2.0 -4.0*a*c<0:
        return None,None
    x1=(-b+(b**c)**0.5)/(2.0*a)
    x2=(-b-(b**2.0 -4.0*a*c)**0.5)/(2.0*a)
        return x1,x2
r1,r2=root(1,2,3)
print(r1,r2)
'''

def print_sum():
    a=1
    b=2
    result = a + b
    print('print_sum() 내부 :', a, '과', b, '의 합은', result, '입니다.')
a = 10 
b = 20 
print_sum()
result = a + b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')
