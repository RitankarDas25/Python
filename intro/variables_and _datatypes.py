# variable is a name given to memory location
"""
this is
multi-line
"""
name = "Ritankar" # string
age = 22 #integer
price=25.99 #floating value

print("my name is : ",name," my age is :",age,price) #prints name age and price

# RULES FOR IDENTIFIERS
# 1) can be combination of upper case, lower case , digits or underscore
# 2) cannot start with digit but can contain digit in between and end
# 3) cannot use !,#,@,%,$
# 4) can be of any length

print(type(name)) # prints <class 'str'> (it prints datatype)
print(type(age)) # prints <class 'int'>
print(type(price)) # prints <class 'float'>

#datatypes - 1) integers 2) String 3) Float 4)Boolean (True,False) 5) none
name1 = 'RD'
name2 ="RD"
name3 ='''RD'''# different ways to declare string
flag = True
a = None
print(type(flag))#<class 'bool'>
print(type(a))#<class 'NoneType'>

# python is case sensitive

a =2 
b=5
sum = a +b
print(sum)

