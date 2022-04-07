"""
Name: [ธารมาส แก้วมณ๊]
SID: [36411760010]
Group: [MIT211]
"""

#Assignment 4
#Computer Programming 2/2564
#MIT211-2

#4.1

#t = int(input("Enter number: "))
#count = 0
#while count <t:
    #if t % 5 == 0:
       #print(f'The result is : ', count)
       #count = count+5


#4.2

#number = int(input("Enter number: "))
#a = []
#while True:
    #x = int(input())
    #if x == number:
        #break
    #a.append(x)
#print(a)



#4.3

# Assignment_4.1
#f = open("A4Q1.txt", 'a')
#t = int(input("Enter number: "))
#count = 0
#while count < t:
    #if t % 5 == 0:
        #count = count + 5
    #f.write(str(count)+'\n')
#f.close()

# Assignment_4.2
f = open("A4Q2.txt", 'a')
number = int(input("Enter number: "))
a = []
while True:
    x = int(input())
    if x == number:
        break
    a.append(x)
print(a)
f.write(str(a)+'\n')
f.close()

