#strings are immutable in python
str1="jh's"
str2='jkhdc"hello"'
str3='''kuhcngxuf"hi"'bye'hg'''#includes"" and '' in the string
print(str3)
# escape sequences - \n = next line , \t - tab 

#concatenation
print("hello"+"world")
a = "a"
b ="b" + a
print(b)

#length
print(len(str1)) #prints 4

#indexing
a="abcdef"
print(a[1])# prints b( we cannot change string using indexing)

#Slicing
print(a[1:3]) #prints bc includes starting index excludes ending index
print(a[:3])# same as a[0:3]
print(a[3:])# same as a[3:len(a)]
# negative index
# a  b  c  d  e  f
#-6 -5 -4 -3 -2 -1
print(a[-3:-1]) # prints de
