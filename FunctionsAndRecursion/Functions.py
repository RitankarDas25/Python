# Block of statements that perform a specific task
def sum(a,b): # def is keyword that defines a function
    return a + b
print(sum(2,3)) # function call

#Waf to print list
def print_list(list):
    for item in list:
        print(item,end=" ") # end =" "is an argument of print function that prints elements in same line
arr=[1,2,3,4,5]
print_list(arr)
print()

# WAF to convert USD to INR

def to_INR(usd):
    return usd*83
usd = int(input("enter USD : "))
print("$",usd," = ",to_INR(usd),"INR")