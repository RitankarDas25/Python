age=21
if(age>18):
    print("valid")
elif(age == 18):
    print("perfect") #indentation
else:
    print("invalid")

marks = int(input("enter marks : "))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print(grade)