"""
Name: {นางสาวธารมาส แก้วมณี}
ID: {364211760010}
Group: {MIT211}
"""
"""
Question 3:
ให้ Print ตัวเลขระหว่าง 1 - 100 โดยที่
ถ้าตัวเลขหารด้วย 3 ลงตัว ให้ Print ว่า MT
ถ้าตัวเลขหารด้วย 5 ลงตัว ให้ Print ว่า MIT
ถ้าตัวเลขหารด้วย 3 และ 5 ลงตัว ให้ Print ว่า SAIYAI
โดย Output 1 - 15 จะออกมาในลักษณะนี้  
พร้อมทั้งเขียนผลลัพท์ลงในไฟล์ชื่อ final4.txt          
(5 คะแนน)
Result:
1
2
MT
4
MIT
MT
7
8
MT
MIT
11
MT
13
14
SAIYAI
"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("SAIYAI")
    elif i % 3 == 0:
        print("MT")
    elif i % 5 == 0:
        print("MIT")
    else:
        print(i)

f = open("final4.txt", 'a')
a = [ ]
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("SAIYAI")
    elif i % 3 == 0:
        print("MT")
    elif i % 5 == 0:
        print("MIT")
    else:
        print(i)