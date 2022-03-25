# Assignment 3 Q1

def myfunc(a,b,c):
    return a+b+c

result = myfunc(10,20,30)
print('The result from function: ',result)

def getNumber():
    mynumber = []
    for x in range(3):
        mynumber.append(int(input(f'Enter integer [{x+1}]: ')))
    return mynumber
def totalValue(var):
    total = 0
    for x in var:
        total+=x
    return total

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The summation of those integer is: {totalValue(mynum)}')

def getNumber():
    mylist = []
    for x in range(1):
        mylist.append(int(input(f'Enter integer : ')))
    return mylist
def myfunction(var):
    total = 0
    for x in var:
        e = x ** 2
        total = total + e
    return total

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The result of squaring  is: {myfunction(mynum)}')

op = ['+', '-', '*', '/']
def calculator():
    a = input('Enter A : ')
    b = input('Enter B : ')
    op = input('Enter OP :')
    if op == '+':
        return 'a+b'
    elif op == '-':
        return 'a-b'
    elif op == '*':
        return 'a*b'
    else:
        return 'a/b'

cal = calculator()
print(cal)

def getNumber():
    listA = []
    for x in range(5):
        listA.append(int(input(f'Enter integer [{x+1}]: ')))
    return listA

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The lowest number is: {min(mynum)}')
print(f'The maximum number is: {max(mynum)}')

def getPTD():
    sumPID = [int(x) for x in input(f'Enter PID : ').split()]
    return sumPID

def getFortune(*var):
    resultlist = []
    for x in var:
        if x % 2 == 0:
            resultlist.append('Your fortune is good')
        else:
            resultlist.append('Your fortune is very good')
    return resultlist

PID = getPTD()
print(f'The data from user: {sum(PID)}')
print(f'The prediction result is: {getFortune(sum(PID))}')

