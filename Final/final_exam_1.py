"""
Name: {นางสาวธารมาส แก้วมณี}
ID: {364211760010}
Group: {MIT211}
"""
"""
Question 1:
จงเขียนโปรแกรมรับเลขจำนวนเต็ม 0 - 9 ไปเรื่อยๆ 
โปรแกรมจะหยุดรับก็ต่อเมื่อผู้ใช้ป้อนเลขผิด เช่น ป้อนเลข 10 เลข -1 หรือเลขอื่นๆ ท
ี่อยู่นอกขอบเขต 0 – 9 เมื่อโปรแกรมหยุดรับค่า 
ให้แสดงผลว่าเลข 0 - 9 มีการป้อนเลขเข้าไปกี่ครั้ง 
และเขียนผลลัพท์ลงในไฟล์ชื่อ final2.txt 
(5 คะแนน)
"""
a = [ ]
while True:
    x = int(input())
    if x == 10:
        break
    a.append(x)
print(a)

f = open("final1.txt", 'a')
a = [ ]
while True:
    x = int(input())
    if x == 10:
        break
    a.append(x)
print(a)