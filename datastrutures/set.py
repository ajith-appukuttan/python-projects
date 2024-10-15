fruitsSet={"apple","banana","cherry"}
fruitsSet.add("dates")
#print("apple" in fruitsSet)


# a="apple"
# print(set(a))


a = 'abracadabra'
# b =  {x for x in a if x not in 'abc'}
# print(b)
# print(list(set(a))==list(a))

lista=list(a);
# print(lista)
newDicst={}

for i in lista :   
    newDicst[i]=lista.count(i)
#find the number of occurences of each character in a string
print(newDicst)
#find highest occurence in a dictionary
print(max(newDicst,key=newDicst.get))  
print(min(newDicst,key=newDicst.get))





     
   
