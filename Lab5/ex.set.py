# set

myset = {'apple','banana','cherry'}
print(myset)
print(type(myset))
print(len(myset))

# access data in set
# for
for x in myset:
    print(x)

# keyword in
print('apple' in myset)  # true
print('mango' in myset)  # false

# add data to set
# add()
myset.add('mango')
print(myset)
# update()
mynum = {10,20,30}
print(mynum)
myset.update(mynum)
print(myset)

# removr data in set
# remove()
myset.remove('banana')
if 'papaya' in myset:
    myset.remove('papaya')
else:
    print('sey has no item "papaya"')
print(myset)

# discard()
myset.discard(20)

# pop()
x = myset.pop()
print(x)
print(myset)

# del keyword
del mynum
#print(mynum)

#clear data in set
#claer()
myset.clear()
print(myset) # {}

myset.add(100)
print(myset)




