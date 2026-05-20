'''
객체 지향 프로그래밍: 데이터와 메서드를 하나의 객체단위로 묶어 모델링
절차적 프로그래밍: 순차적인 처리
그래픽 사용자 인터페이스: 사용자가 시각적인 요소를 통해 상호작용할 수 있는 지표

클래스: 객체의 속성과 함수 정의한 집합체
객체: 클래스를 바탕으로 구현할 수 있는 대상
인스턴스: 실체화된 객체
클래스의 속성:객체가 가진 상태나 특징
클래스의 동작: 객체가 수행할 수 있는 기능이나 행위
'''
'''
class Dog:
    def bark(self):
        print('멍멍!')

my_dog=Dog()
my_dog.bark()
'''
'''
class Dog:
    def __init__(self, name):
        self.name=name
    def bark(self):
        print('멍멍!')
my_dog=Dog('Jindo')
my_dog.bark()
'''
'''
class Dog:
    def __init__(self, name):
        self.name=name

    def __str__(self):
        return 'Dog(name={})'.format(self.name)

my_dog=Dog('Jindo')
print('my_dog의 정보:', my_dog)
'''
'''
n=100
m=100
if n is m:
    print('n is m')
else:
    print('n is not m')
#동일한 객체 주소 100이 n과 m에 주어짐.
'''
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print('v1 * v2 =', v1 * v2)
print('v1 / v2 =', v1 / v2)

v1_new = Vector(10, 20)
print('-v1 =', -v1_new)
'''
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length_squared(self):
        return self.x**2 + self.y**2

    def __gt__(self, other):
        return self.length_squared() > other.length_squared()

    def __ge__(self, other):
        return self.length_squared() >= other.length_squared()

    def __lt__(self, other):
        return self.length_squared() < other.length_squared()

    def __le__(self, other):
        return self.length_squared() <= other.length_squared()

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print('v1 > v2 =', v1 > v2)
print('v1 >= v2 =', v1 >= v2)
print('v1 < v2 =', v1 < v2)
print('v1 <= v2 =', v1 <= v2)
'''
'''
class Rect:
    def __init__(self, width, height):
        self.width=width
        self.height=height

r1=Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['width'])
'''

class Rect:
    def __init__(self, width, height):
        self.width=width
        self.height=height

r1=Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])
