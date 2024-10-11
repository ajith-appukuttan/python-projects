# Python Data Types

# 1. Numeric Types
# Integer
int_var = 10
print(f"Integer: {int_var}, Type: {type(int_var)}")

# Float
float_var = 10.5
print(f"Float: {float_var}, Type: {type(float_var)}")

# Complex
complex_var = 1 + 2j
print(f"Complex: {complex_var}, Type: {type(complex_var)}")

# 2. Sequence Types
# String
str_var = "Hello, World!"
print(f"String: {str_var}, Type: {type(str_var)}")

# List
list_var = [1, 2, 3, 4, 5]
print(f"List: {list_var}, Type: {type(list_var)}")

# Tuple
tuple_var = (1, 2, 3, 4, 5)
print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")

# 3. Mapping Type
# Dictionary
dict_var = {"name": "Kamal", "age": 30}
print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")

# 4. Set Types
# Set
set_var = {1, 2, 3, 4, 5}
print(f"Set: {set_var}, Type: {type(set_var)}")

# Frozenset
frozenset_var = frozenset({1, 2, 3, 4, 5})
print(f"Frozenset: {frozenset_var}, Type: {type(frozenset_var)}")

# 5. Boolean Type
bool_var = True
print(f"Boolean: {bool_var}, Type: {type(bool_var)}")

# 6. Binary Types
# Bytes
bytes_var = b"Hello"
print(f"Bytes: {bytes_var}, Type: {type(bytes_var)}")

# Bytearray
bytearray_var = bytearray(5)
print(f"Bytearray: {bytearray_var}, Type: {type(bytearray_var)}")

# Memoryview
memoryview_var = memoryview(bytes(5))
print(f"Memoryview: {memoryview_var}, Type: {type(memoryview_var)}")