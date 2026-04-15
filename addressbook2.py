import json


#주소록데이터
addressbook= dict()

name=None
while(True):
    name=input('이름을 입력하세요:')
    if(name=='끝'):
        break
    phoneNum=input('전화번호를 입력하세요:')

    addressbook[name]= phoneNum

#1. 파일로 저장
with open('addressbook.json','w', encoding='utf-8') as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)


print('주소록이 저장되었습니다')

'''
#2.파일에서 다시 불러오기
with open ('addressbook.json', 'r', encoding='utf-8') as f:
    addressbook= json.load(f)

print('불러온 주소록:', addressbook)
print('김영호 번호:', addressbook['김영호'])

'''
