i=0
while i<5:
    print(i)
    i+=1

# wap to print elements of list
list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print(list[i])
    i+=1

# search a number x in tuple
tup=(1,4,9,16,25,36,49,64,81,100)
x =int(input("enter number to be searched : "))
i=0
while i<len(tup):
    if(tup[i]==x):
        print("found")
        break
    i+=1
# break is used to terminate the loop
# continue is used to go to next iteration