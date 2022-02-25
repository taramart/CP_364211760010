# Loop - while, for


"""
พิมพ์ข้อมความ Hello 100 ครั้ง
"""


# while
# count = 1
# while count <=100:
#     print('Hello', count)
#     count+=1 # count = count+1

# # for
#  print('print from for loop:')
#
# for x in range(100): # range(100)--> 0,1,2,3...99
#     print('Hello',x)

"""
เริ่มต้นที่ 0 เพิ่มค่าครั้งละ 1
"""
for x in range(5): # 0 1 2 3 4
    print(x)

"""
เริ่มต้นที่ 2 เพิ่มค่าครั้งละ 1
"""

for x in range(2,10): # 2 3 4 5 6 7 8 9
     print(x)

"""
เริ่มต้นที่ 2 เพิ่มค่าครั้งละ 3
"""
for x in range(2,30,3): # 2 5 8 11 14 17 20 23 26 27
    print(x)