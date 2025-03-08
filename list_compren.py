#List Comprehension: A Concise way to create lists in python.
#                   Compact and easier than traditional loops
#                   [Expression for value in iterable if condition]

numbers=[1,2,3,4,-1,-4,-9]
even=[x for x in numbers if x%2==0]
print(even)
odd=[x for x in numbers if x%2==1]
print(odd)