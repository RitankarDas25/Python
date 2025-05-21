# Arithmetic operator - + ,-,*,/,%,** 
a =5
b=2
print(a+b,a-b,a*b,a/b,a%b,a**b)# / always gives float value , ** is power operator a to the power b
#relational operator - == , != ,>,<,>=,<=
print(a==b,a!=b,a>b,a<b,a>=b,a<=b) #returns boolean value
# assignment operator - =,+=,-=,*=,/=,%=,**= it means a= a**b
c=10
#print(c+=10) gives syntax error
c+=10
print(c) # 20
c-=10
print(c) #10
c*=10
print(c) #100
c/=10
print(c) # 10.0
c%=10
print(c) #0.0
c =10
c**=10 #10000000000
print(c)
#logical operators - not , and ,or
print(not True) # print false
print(not(10<1)) #prints true
print(True and False) #prints false
print(True or False) #prints true