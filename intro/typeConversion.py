#1) type conversion - interpreter does it automaticaly
#2)type casting - done by programmer

# TYPE CONVERSION
a=2
b=4.25
sum = a+ b # type converted to float
print(sum)
a = "2"
#sum = a + b gives error-TypeError: can only concatenate str (not "float") to str
#print(sum)

#TYPE CASTING
a,b=1,"2"
c = int(b)# type casted to int
print(a+c)
#x ="fvykv"
#y=float(x) gives error as characters cannot be stored
y = str(a) # converts to string