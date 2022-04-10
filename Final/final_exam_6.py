"""
Name: {นางสาวธารมาส แก้วมณี}
ID: {364211760010}
Group: {MIT211}
"""
"""
Quesiton 6:
เขียนโปรแกรมเพื่อนับสระในภาษาอังกฤษ (Vowels: a e i o u) 
โดยรับข้อความจากผู้ใช้ จากนั้นให้โปรแกรมแสดงผลว่าจากข้อความดังกล่าว
มีสระแต่ละตัวมีจำนวนเท่าไร

Example:

Input message:  The National Vaccine Board approved a 
policy with the additional target of procuring 150 million 
doses of COVID-19 vaccines by 2022

Result:
a = 10
e = 7
I = 11
o = 11
u = 1 

"""
a = []
data = ['a', 'e', 'i' , 'o' , 'u']
count = 0

for x in range(len(data)):
    for y in range(len(data[x])):
        if( data[x][y].islower() ):
            count = count + 1

print('Lowercase letters = '+str(count))
