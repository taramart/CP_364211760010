"""
เขียนโปรแกรม Login โดยรับ Input จากชื่อผู้ใช้
คือ username และ password หากผู้ใช้กรอกข้อมูลถูกต้อง
ให้แสดงข้อความ "Welcome {name}"
แต่ถ้าไม่ถูกต้องให้ผู้ใช้กรอกข้อมูลใหม่
หากกรอกข้อมูลผิดครบ 3 ครั้ง ให้แสดงข้อความ
"Your account has been locked, please coutact admin."
"""

user = 'admin'
password = '1234'

count = 0
while count < 3:
    u = input('enter username: ')
    p = input('enter password: ')
    if u == user and p == password:
        print(f'Hello, {u}')
        break
    else:
        print(f'username or password is not correct.{count+1}')
        if count < 2:
            print(f'pless, login again.')
        count+=1
else:
    print('Your account has been locked, please coutact admin.')