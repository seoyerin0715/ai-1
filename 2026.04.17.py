'''
student1={'name':'민수','score':85}
student2={'name':'지영','score':92}

def get_grade(student):
    if student['score']>=90:
        return 'A'
    elif student['score']>=80:
        return 'B'
    else:
        return 'C'
print(get_grade(student1))
print(get_grade(student2))
'''

class Student:
    def __init__(self,name,score):
        self.__name= name
        self.__score= score

    def __str__(self):
        return '이름:{}, 점수:{}'.format(self.__name, self.__score)

    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=80:
            return 'B'

민수=Student('민수', 85)
지영=Student('지영', 92)


#민수.name=name
#민수.socre=score
print(민수)
print(민수.__name)

#print(민수.get_grade())
#print(지영.get_grade())

'''
class Phone:
    def __init__(self, brand, battery):
        self.brand= brand
        self.battery= battery

    def use(self, minutes):
        self.battery-=0.5*minutes
        print(self.battery)
        
    def charge(self, minutes):
        self.battery+=minutes
        print(self.battery)
        
my_phone= Phone('galaxy', 80)
my_phone.use(30)
my_phone.charge(20)
'''
