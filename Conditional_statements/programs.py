#odd-even
i=int(input("enter num: "))
if(i%2==0):
    print("even")
else:
    print("odd")

#greatest of 3 num
a=int(input("enter num 1: "))
b=int(input("enter num 2: "))
c=int(input("enter num 3: "))
if(a>=b and a>=c):
    print(a," is largest")
elif(b>=c):
    print(b," is largest")
else:
    print(c," is largest")
    
#if multiple of 7
x =int(input("enter num: "))
if(x%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")


