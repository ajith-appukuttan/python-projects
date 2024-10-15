def make_incrementor(n):
    return lambda x: x + n

def make_newstring(name):
    return lambda x: x + name

full_name = make_newstring(" John")
print(full_name("Doe"))
print(full_name("Smith"))
