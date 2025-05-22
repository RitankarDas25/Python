#python can read write from files
#text files - .txt, .docx, .log
#binary files - .mp4,.mov, .png , .jpeg

# f = open("file_name and path","mode")
# mode - r: read or w: write or x: create new file and write a : append at end of file b: binary mode t:text mode +: read and write
#data= f.read()
#f.close()
# we can read only once from a file which it opened once to re read we need to close and re open the file
import os

f = open("C:\\Users\\User\\OneDrive\\Desktop\\ml\\python\\FileHandling\\demo.txt", "r")
data = f.read()
print(data)
print(type(data))

#data1 = f.read(5) #reads first 5 characters
#print(data1)

#line1 = f.readline() # reads first line
#print(line1)

f.close()

f = open("C:\\Users\\User\\OneDrive\\Desktop\\ml\\python\\FileHandling\\demo.txt", "w") # if a file doesnt exist write mode creats the file
f.write("i am learning python 123")
f.close()

f = open("C:\\Users\\User\\OneDrive\\Desktop\\ml\\python\\FileHandling\\demo.txt", "a")
f.write(" \n new data is appended")
f.close()

#with syntax - better way to code it automatically closes the file
with open("C:\\Users\\User\\OneDrive\\Desktop\\ml\\python\\FileHandling\\demo.txt", "r") as f:
    data = f.read()
    print(data)

#deleting a file
# os module is needed to be imported to perform deletion

os.remove("filename or path") # deletes the file