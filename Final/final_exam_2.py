"""
Name: {นางสาวธารมาส แก้วมณี}
ID: {364211760010}
Group: {MIT211}
"""
"""
Question 2:
จงเขียนโปรแกรมหาตัวเลขที่เลข 3 หรือ 5 หรือ 7 หารลงตัว จากเลข 1 ถึงตัวเลขที่ป้อนทางคีย์บอร์ด โดยแสดงตัวเลขว่ามีกี่จำนวน 
ต่อด้วยตัวเลขที่หารลงตัวโดยแต่ละตัวคั่นด้วยเว้นวรรค  และเขียนผลลัพท์ที่ได้ลงในไฟล์ชื่อ final1.txt  เช่น
Enter number: 20
The result is 8: 3 5 9 10 12 15 18 20
(5 คะแนน)
"""
a = []

t = int(input("Enter number: "))
count = 0
while count <t:

    if t % 3 == 0:
       print(f'The result is : ', count)
       count = count+3
    elif t % 5 == 0:
       print(f'The result is : ', count)
       count = count+5
    elif t % 7 == 0:
       print(f'The result is : ', count)
       count = count+7

    if t % 3 == 0 and t % 5 == 0 and t % 7 == 0:
        print()