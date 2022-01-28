# list comprehension

mylist = [12, 34, 65, 77, 54, 88, 25, 99, 20, 44]
print(mylist, len(mylist))

#เลือกข้อมูลจาก mylist
# โดยเลือกเฉพาะข้อมูลที่มากกว่าหรือเท่ากับ 50
newlist = [x for x in mylist if x >= 50]
print(newlist)

#เลือกข้อมูลจาก mylist
#โดยเลือกเฉพาะข้อมูลที่มากกว่าหรือเท่ากับ 50 และ น้อยกว่า 80
ืnewlist = ['x for x in mylist if x >= 50 and x < 80']
print(newlist)

# จากข้อมูลใน mylist ให้ทำการเปลี่ยนข้อมูล
# ที่มีค่ามากกว่า 50 เป็น 50 ทั้งหมด
print(mylist)
newlist = ['x if x<50 else x =50 for x in mylist']
print(newlist)

# reverse data in list
mylist.reverse()
print(mylist)

# sort list
# low to high
mylist.sort()
print(f'sort low to high: {mylist}')
# high to low
mylist.sort(reverse=True)
print(f'sort high to low: {mylist}')

#join list
x = [10,20,30]
y = ['a','b','c']

z = x+y
print(z)

x.extend(y)
print(x)

