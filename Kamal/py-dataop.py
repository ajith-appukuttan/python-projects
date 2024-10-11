# Integer operations






# - Clear: Remove all items from the dictionary using dict.clear().
# - Update: Update the dictionary with key-value pairs from another dictionary using dict.update().
# - Pop: Remove the value for a specified key and return it using dict.pop(key).
# - Popitem: Remove and return the last key-value pair using dict.popitem().
# - Setdefault: Retrieve the value for a specified key, and if the key does not exist, insert the key with a specified value using dict.setdefault(key, default).
# - Fromkeys: Create a new dictionary with keys from an iterable and values set to a specified value using dict.fromkeys(iterable, value).

# - Length: Retrieve the number of elements in the tuple using len(tuple).
# - Indexing: Access an element by its index using tuple[index].
# - Slicing: Retrieve a subset of the tuple using tuple[start:end].
# - Count: Count the occurrences of a specified value using tuple.count(value).
# - Index: Find the index of the first occurrence of a specified value using tuple.index(value).

# - Union: Return a set containing all elements from both sets using set1 | set2.
# - Intersection: Return a set containing only elements found in both sets using set1 & set2.
# - Difference: Return a set containing elements in the first set but not in the second using set1 - set2.
# - Symmetric Difference: Return a set containing elements in either set but not in both using set1 ^ set2.






# - Keys: Retrieve all keys in the dictionary using dict.keys().
# - Values: Retrieve all values in the dictionary using dict.values().
# - Items: Retrieve all key-value pairs in the dictionary using dict.items().
# - Get: Retrieve the value for a specified key using dict.get(key).
# - Add new key-value pair: Add a new key-value pair to the dictionary using dict[key] = value.


"""
This script demonstrates various operations in Python for different data types including integers, floats, complex numbers, strings, lists, dictionaries, tuples, and sets.

Integer operations:
- Addition, Subtraction, Multiplication, Division, Floor Division, Modulus, Exponentiation

Float operations:
- Addition, Subtraction, Multiplication, Division

Complex number operations:
- Addition, Subtraction, Multiplication, Division

String operations:
- Concatenation, Repetition, Length, Substring

List operations:
- Concatenation, Repetition, Length, Append, Pop, Insert, Remove, Reverse, Sort

Dictionary operations:
- Keys: Retrieve all keys in the dictionary.
- Values: Retrieve all values in the dictionary.
- Items: Retrieve all key-value pairs in the dictionary.
- Get: Retrieve the value for a specified key.
- Add new key-value pair: Add a new key-value pair to the dictionary.

Tuple operations:
- Length, Indexing, Slicing

Set operations:
- Union, Intersection, Difference, Symmetric Difference
"""
a = 10
b = 3
print("Integer Operations:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print()

# Float operations
x = 10.5
y = 2.5
print("Float Operations:")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print()

# Complex number operations
c1 = complex(2, 3)
c2 = complex(1, 4)
print("Complex Number Operations:")
print(f"Addition: {c1} + {c2} = {c1 + c2}")
print(f"Subtraction: {c1} - {c2} = {c1 - c2}")
print(f"Multiplication: {c1} * {c2} = {c1 * c2}")
print(f"Division: {c1} / {c2} = {c1 / c2}")
print()

# String operations
str1 = "Hello"
str2 = "World"
print("String Operations:")
print(f"Concatenation: {str1} + {str2} = {str1 + ' ' + str2}")
print(f"Repetition: {str1} * 3 = {str1 * 3}")
print(f"Length: len({str1}) = {len(str1)}")
print(f"Substring: {str1}[1:4] = {str1[1:4]}")
print()

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List Operations:")
print(f"Concatenation: {list1} + {list2} = {list1 + list2}")
print(f"Repetition: {list1} * 2 = {list1 * 2}")
print(f"Length: len({list1}) = {len(list1)}")
print(f"Append: {list1}.append(4) = ", end="")
list1.append(4)
print(list1)
print()
print(f"Pop: {list1}.pop() = {list1.pop()}")
print(f"After Pop: {list1}")
list1.insert(1, 10)
print(f"Insert: {list1}.insert(1, 10) = {list1}")
list1.remove(10)
print(f"Remove: {list1}.remove(10) = {list1}")
list1.reverse()
print(f"Reverse: {list1}.reverse() = {list1}")
list1.sort()
print(f"Sort: {list1}.sort() = {list1}")

# Dictionary operations
dict1 = {'a': 1, 'b': 2}
print("Dictionary Operations:")
print(f"Keys: {dict1.keys()}")
print(f"Values: {dict1.values()}")
print(f"Items: {dict1.items()}")
print(f"Get value for key 'a': {dict1.get('a')}")
dict1['c'] = 3
print(f"Add new key-value pair 'c': 3 -> {dict1}")
print()
# Method usage of dictionary
print("Method Usage of Dictionary:")
# clear()
dict1.clear()
print(f"Clear: dict1.clear() -> {dict1}")

# update()
dict1 = {'a': 1, 'b': 2}
dict1.update({'b': 3, 'c': 4})
print(f"Update: dict1.update({{'b': 3, 'c': 4}}) -> {dict1}")

# pop()
value = dict1.pop('b')
print(f"Pop: dict1.pop('b') -> {value}, dict1 -> {dict1}")

# popitem()
key, value = dict1.popitem()
print(f"Popitem: dict1.popitem() -> ({key}, {value}), dict1 -> {dict1}")

# setdefault()
value = dict1.setdefault('d', 5)
print(f"Setdefault: dict1.setdefault('d', 5) -> {value}, dict1 -> {dict1}")

# fromkeys()
keys = ['e', 'f', 'g']
dict2 = dict.fromkeys(keys, 0)
print(f"Fromkeys: dict.fromkeys({keys}, 0) -> {dict2}")

# Tuple operations
tuple1 = (1, 2, 3)
print("Tuple Operations:")
print(f"Length: len({tuple1}) = {len(tuple1)}")
print(f"Indexing: {tuple1}[1] = {tuple1[1]}")
print(f"Slicing: {tuple1}[0:2] = {tuple1[0:2]}")
print()
# Tuple method usage
tuple2 = (1, 2, 3, 2, 4, 2)
print("Tuple Method Usage:")
print(f"Count: {tuple2}.count(2) = {tuple2.count(2)}")
print(f"Index: {tuple2}.index(3) = {tuple2.index(3)}")
# Since tuples are immutable, we cannot directly add or remove elements.
# However, we can convert the tuple to a list, perform the operations, and convert it back to a tuple.

# Add element to tuple
tuple3 = tuple1 + (4,)
print(f"Add: {tuple1} + (4,) = {tuple3}")

# Remove element from tuple
tuple4 = tuple(item for item in tuple1 if item != 2)
print(f"Remove: {tuple1} without 2 = {tuple4}")

# Sort tuple
sorted_tuple = tuple(sorted(tuple2))
print(f"Sort: sorted({tuple2}) = {sorted_tuple}")

# Filter tuple (e.g., filter out all elements less than 3)
filtered_tuple = tuple(item for item in tuple2 if item >= 3)
print(f"Filter: elements >= 3 in {tuple2} = {filtered_tuple}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set Operations:")
print(f"Union: {set1} | {set2} = {set1 | set2}")
print(f"Intersection: {set1} & {set2} = {set1 & set2}")
print(f"Difference: {set1} - {set2} = {set1 - set2}")
print(f"Symmetric Difference: {set1} ^ {set2} = {set1 ^ set2}")
print()
# Set method usage
set3 = {1, 2, 3}
print("Set Method Usage:")

# add()
set3.add(4)
print(f"Add: set3.add(4) -> {set3}")

# remove()
set3.remove(2)
print(f"Remove: set3.remove(2) -> {set3}")

# discard()
set3.discard(3)
print(f"Discard: set3.discard(3) -> {set3}")

# pop()
popped_value = set3.pop()
print(f"Pop: set3.pop() -> {popped_value}, set3 -> {set3}")

# clear()
set3.clear()
print(f"Clear: set3.clear() -> {set3}")

# update()
set3.update({5, 6})
print(f"Update: set3.update({{5, 6}}) -> {set3}")

# intersection_update()
set3 = {1, 2, 3}
set4 = {2, 3, 4}
set3.intersection_update(set4)
print(f"Intersection Update: set3.intersection_update(set4) -> {set3}")

# difference_update()
set3 = {1, 2, 3}
set3.difference_update(set4)
print(f"Difference Update: set3.difference_update(set4) -> {set3}")

# symmetric_difference_update()
set3 = {1, 2, 3}
set3.symmetric_difference_update(set4)
print(f"Symmetric Difference Update: set3.symmetric_difference_update(set4) -> {set3}")

# issubset()
set5 = {1, 2}
set6 = {1, 2, 3}
print(f"Issubset: {set5}.issubset({set6}) = {set5.issubset(set6)}")

# issuperset()
print(f"Issuperset: {set6}.issuperset({set5}) = {set6.issuperset(set5)}")

# isdisjoint()
set7 = {4, 5}
print(f"Isdisjoint: {set5}.isdisjoint({set7}) = {set5.isdisjoint(set7)}")

# copy()
set8 = set5.copy()
print(f"Copy: {set5}.copy() = {set8}")

# frozenset (immutable set)
frozen_set = frozenset(set5)
print(f"Frozenset: frozenset({set5}) = {frozen_set}")
# More examples of set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("More Set Operations:")
print(f"Union: {set_a} | {set_b} = {set_a | set_b}")
print(f"Intersection: {set_a} & {set_b} = {set_a & set_b}")
print(f"Difference (set_a - set_b): {set_a} - {set_b} = {set_a - set_b}")
print(f"Difference (set_b - set_a): {set_b} - {set_a} = {set_b - set_a}")
print(f"Symmetric Difference: {set_a} ^ {set_b} = {set_a ^ set_b}")

set_c = {7, 8}
set_d = {8, 9, 10}

print(f"Union: {set_c} | {set_d} = {set_c | set_d}")
print(f"Intersection: {set_c} & {set_d} = {set_c & set_d}")
print(f"Difference (set_c - set_d): {set_c} - {set_d} = {set_c - set_d}")
print(f"Difference (set_d - set_c): {set_d} - {set_c} = {set_d - set_c}")
print(f"Symmetric Difference: {set_c} ^ {set_d} = {set_c ^ set_d}")

set_e = {1, 2, 3}
set_f = {4, 5, 6}

print(f"Union: {set_e} | {set_f} = {set_e | set_f}")
print(f"Intersection: {set_e} & {set_f} = {set_e & set_f}")
print(f"Difference (set_e - set_f): {set_e} - {set_f} = {set_e - set_f}")
print(f"Difference (set_f - set_e): {set_f} - {set_e} = {set_f - set_e}")
print(f"Symmetric Difference: {set_e} ^ {set_f} = {set_e ^ set_f}")