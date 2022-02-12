"""
Name: {นางสาวธารมาส แก้วมณี}
SID: {364211760010}
Group: {}
"""

"""
Question 2:
จงเขียนโปรแกรมจาก tuple ที่กำหนดให้
(10 คะแนน)
"""

myTuple = (100,200,300,400,500)  

# แสดงผลข้อมูลใน myTuple ทั้งหมด
print(myTuple)
# แสดงผลข้อมูล 200 จาก myTuple
print(myTuple[1])
# แสดงผลข้อมูล 500 จาก myTuple
print(myTuple[4])
# แสดงผลข้อมูล 500 จาก myTuple โดยใช้ negative index
print(myTuple[-1])
# แสดงผลข้อมูล (200,300,400) โดยใช้ range index
print(myTuple[1:4])
# แสดงผลข้อมูล (400,500) โดยใช้ range index
print(myTuple[3:5])
# แสดงผลข้อมูล (100,200) โดยใช้ range negative index
print(myTuple[0:2])

# แสดงผลข้อมูลใน myTuple ทั้งหมด โดยการใช้ for loop
for x in range(len(myTuple)):
    print(myTuple[x])

# Tuples ไม่สามารถเพิ่มหรือลบข้อมูลได้ แต่สามารถเปลี่ยน Tuples เป็น List เพื่อเพื่อหรือลบข้อมูล
# เปลี่ยน myTuple เป็น List ชื่อ myList
mylist = list(myTuple)
print(mylist,type(mylist),len(mylist))

# เพิ่มข้อมูล 10,20,30 ใน myList
mylist.append(10)
mylist.append(20)
mylist.append(30)

# เพิ่มข้อมูล 40 ใน myList ในตำแหน่งที่ 0
mylist.insert(0,40)
print(mylist)
# เพิ่มข้อมูล 50 ใน myList ในตำแหน่งที่ 3
mylist.insert(3,50)
print(mylist)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(mylist)

# ลบข้อมูล 10
mylist.remove(10)
print(mylist)
# ลบข้อมูล 100
mylist.remove(100)
print(mylist)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(mylist)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
mylist.pop()
# แสดงผลข้อมูลใน myList ทั้งหมด
print(mylist)
# เรียงข้อมูล myList จาก น้อย-มาก
mylist.sort()
# แสดงผลข้อมูลใน myList ทั้งหมด
print(mylist)
# นำข้อมูลใน myList ทั้งหมดบวกรวมกัน และเก็บไว้ในตัวแปร total จากนั้นแสดงตัวแปร total หน้าจอ output

# เปลี่ยน myList เป็น Tuple ในชื่อ myTuple
myTuple = list(mylist)
# แสดงผลข้อมูลทั้งหมดใน myTuple
print(myTuple)