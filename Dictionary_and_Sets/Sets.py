#sets is collection of unordered items
#set is mutable but each element must be unique and immutable,duplicate values are ignored
#list and dictionary cannot be stored in set
arr = {1,2,3,4,"hello"}
print(type(arr))
print(arr)
empty_set = set()
arr.add(7)
arr.remove(2)
arr.pop()
print(arr)
#set1.union(set2) combine both set values
#set1.intersection(set2) combines only common values
