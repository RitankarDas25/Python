a=int(input("enter 1st num: "))
b =int(input("enter 2nd num: "))

flag = True
while(flag):
    c = input("enter operator: ")
    if(c == "+"):
      print("sum =",a+b)
    elif(c == "-"):
        print("diff =",a-b)
    elif(c =="*"):
        print("mul =",a*b)
    elif(c =="/"):
        print("div =",a/b)
    elif(c =="%"):
        print("mod =",a%b)
    elif(c == "**"):
        print("power =",a**b)
    elif(c == "exit"):
        flag=False
    else:
        print("invalid operator")
    