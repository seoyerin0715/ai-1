import json

with open('addressbook.json','r',encoding='utf-8') as f:
    addressbook=json.load(f)


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
