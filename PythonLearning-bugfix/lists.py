import re
my_list=[1,2,3,4,5,6,45,6,5,5]
print(len(my_list))
print(my_list[5])
print(my_list[0:7:2])
print(my_list[::2])

tinylist = [123, 'john']
print(tinylist * 2)

str = 'Hello World!'

print(str[2:5])
print("list: ",list(str))
print("set",set(str))
print("tuple",tuple(str))
print(str.replace(" ",""))


str1= " helo  swapnil   bhaiiii"
print(str1.lstrip())
print (re.sub(' +', ' ',str1))



tuplet=(12,12,13,15,15,13,159,1245)

print("set of my list",set(tuplet))

print("set of my list",set(my_list))

set1=set()
set1.add(10)
set1.add(20)
set1.add(30)
set1.add(40)
set1.add(50)
print("set1 is :",set1)




