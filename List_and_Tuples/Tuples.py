#builtin datatype of immutable sequence of values
tup =(1,2,3,4,5)
print(tup[0])# prints 1
#tup[0]=2  TypeError: 'tuple' object does not support item assignment
# single value tuple should be declared like tup =(1,) if we dont give , then python treats it like integer

#slicing
print(tup[1:3]) # prints 2,3

# methods
print(tup.index(2)) # gives index of 1st occurance of 2
print(tup.count(2)) # gives count of 2
