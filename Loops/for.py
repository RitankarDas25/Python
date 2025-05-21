list=[1,2,3,4]
for i in list:
    print(i)
# range() it returns sequence of numbers starting from 0 by default and with step size 1 by defaut
# range(start,stop,step value)

# we cannot leave a loop empty we have to write "pass" inside it
print(range(5)) # prints (0,5)
for i in range(5,0,-1):
    print(i)
for i in range(0,10,2):
    print(i) # prints all even numbers till 10 (10 not included)

#wap to find factorial

n = int(input("enter number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)