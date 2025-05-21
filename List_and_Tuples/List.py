#List is a builtin datatype that stores set of values and it is mutable
#it is hetrogeneous
marks=[1,2,3,4]
stud=["hel",48,"oho",83.93,True]
print(stud) #prints whole list
print(len(marks)) # prints length of list
print(marks[1],stud[4]) # indexing
marks[1]=10 #changing at index 1
print(marks)

#list slicing
print(marks[1:3]) #prints 10,3
print(marks[:3]) #prints 1,10,3
print(marks[-3:-1]) #prints 10,3

#list methods
marks.append(5) # add 5 at last
print(marks)
marks.sort() # sorts in ascending order
print(marks)
#stud.sort() gives error as cannot compare int and string
#print(stud)
marks.sort(reverse=True) #sorts in decending order
print(marks)
marks.reverse() #reverses the list
print(marks)
marks.insert(1,6)
print(marks) # inserts element at index 1 
marks.remove(6)
print(marks) # removes 1st ocurrence of element
marks.pop(3)
print(marks) # removes elements at index 3
