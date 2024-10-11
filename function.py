# def my_function(*kids):
#   print(type(kids))
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function1(**kid): #passing object
#   print(type(kid))
#   #passing object
#   print("The youngest child is " + kid["kid3"])

# my_function1(kid1="Emil",kid3="Tobias",kid2="Linus")


#Positional-overrides
# def my_function2(name, age,sex,/):
#   print(name)

# my_function2(age="John", name=36,sex="M")

# def my_function(*, x,y):
#   print(x)

# my_function(y=7,x=8)


# #Combine Positional-Only and Keyword-Only

# def my_functionx(a, b, /, *, c, d):
#   print(d)
#   #print(a + b + c + d)

# my_functionx(5, 6, d = 7, c = 8)



# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(3)



print(all([])) #True

a=["apple","banana","cherry"]
tuple1=tuple(a);
print(tuple1)