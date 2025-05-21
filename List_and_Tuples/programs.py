# wap to enter 3 movies and store them in a list

movies =[]
movies.append(input("enter movie 1 :"))
movies.append(input("enter movie 2 :"))
movies.append(input("enter movie 3 :"))
print(movies)

# wap to check if list is palindromic or not eg: [1,"abc","abc",1]

a=[1,2,3,2,1]
b =a.copy()
b.reverse()
if(a ==b):
    print("palindrome")
else:
    print("not palindrome")


# wap to count A in tuple

tup=("C","D","A","A","B","B","A")
print("number of A is = ",tup.count("A"))

#wap to store the above values in a list and sort them
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)
