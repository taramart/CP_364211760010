# Lab 8 Exercise

"""
จงกำหนดฟังก์ชัน ชื่อ "getNumber()" เพื่อรับข้อมูลจำนวนเต็มจากผู้ใช้
5 จำนวน และแสดงผลทางจอภาพ จากนั้นให้กำหนดฟังก์ชั่นต่อไปนี้
และ กำหนดฟังก์ชันชื่อ "totalValue()" เพื่อหาผมรวมของตัวเลขทั้งหมด
แสดงผลทางจอภาพ
"""

def getNumber():
    mynumber = []
    for x in range(5): # x ==> 0 1 2 3 4
        mynumber.append(int(input(f'Enter integer [{x+1}]: ')))
    return mynumber

def totalValue(var):
    total = 0
    for x in var:
        total+=x
    return total

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The summation of '
      f'thoese integer is: {totalValue(mynum)}')