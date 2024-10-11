fruits=["apple","oranges","banana"]
print(fruits)
length=fruits.__len__()
i=0
while(i<length):
    print(fruits[i])
    i+=1
fruits.pop()
fruits.append("blueberry")
print(fruits)
fruits.sort()
print(fruits)


mylist = fruits.copy()
mylist.remove("apple")
print(mylist)
print(fruits)
