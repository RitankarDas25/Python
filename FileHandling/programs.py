# create a file practice.txt and enter -
# hi everyone
# we are learning file I/O
# using java
# i like programming in java
# WAF to replace all java with python
# search if the word "learning" exist

with open("practice.txt","w") as f:
    f.write("Hi everyone \n we are learning File I/O \n using java \n I like programming in java")

def replace_word():
    with open("practice.txt","r") as f:
        data=f.read() # reading the data
    new_data=data.replace("java","python")  # replacing java with python and storing in new string
    print(new_data)
    with open("practice.txt","w") as f:
        f.write(new_data)  # overwriting the file with new string

def find_word(x): # function to find word in file
    with open("practice.txt","r") as f:
     data=f.read()
     if(x in data): # returns false if not found
         print("found")
     else:
            print("not found")

replace_word()
find_word(input("enter word to find: "))

#wap to print the count of even numbers in file

with open("C:\\Users\\User\\OneDrive\\Desktop\\ml\\python\\FileHandling\\num.txt","r") as f :
    data = f.read()
    print(data)
    count=0
    nums=data.split(",") # returns a list with elements after spliting string with ","
    for val in nums :
        if(int(val)%2 ==0): # check for even
            count+=1
    print(count)