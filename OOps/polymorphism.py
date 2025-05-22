#operator overloading - same operator different use
print(1+3)
print("a"+"b")
print([1,2,3]+[4,5,6])

#dunder functions
#a+b - a.__add__(b)
#a-b - a.__sub__(b)
#a*b - a.__mul__(b)
#a/b - a.__truediv(b)
#a%b - a.__mod____(b)

#creating class for complex numbers
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def show(self):
        print(self.real,"i +",self.img,"j")

    #def add(self,num2): #traditional way using simple function
    #    newreal=self.real + num2.real
    #    newimg = self.img + num2.img
    #    return Complex(newreal,newimg)

    def __add__(self,num2): #dunder functions
        newreal=self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal,newimg)
    
    def __sub__(self,num2): #dunder functions
        newreal=self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal,newimg)

num1 = Complex(2,4)
num1.show()
num2=Complex(5,2)
num2.show()
#num3=num1.add(num2)
num3=num1+num2 # dunder add function is called
num3.show()
num4=num1-num2 # dunder sub function is called
num4.show()