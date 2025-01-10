#delete keyword
# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("falsi")
# print(s1.name)
# s2=Student("dhruvi")
# print(s2.name)
# del s1
# print(s1.name)


#private keyword
# class Acc:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass     #for the private usetwo underscore before object name
#     def acc(self):
#         print("password",self.__acc_pass)
     
# s1 = Acc(12345,"abcd")
# print(s1.acc_no)
# s1.acc()

# class Person:
#     __name ="falsi"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()
# s1=Person()


#inheritance
#single 
# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped..")

# class toyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# s1=toyotaCar("fortuner")
# s2=toyotaCar("prius")
# print(s1.name)
# print(s1.start())
# print(s2.color)

#multi-level
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped..")

# class ToyotaCar(Car):
#     color="black"
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type

# s1=Fortuner("ev")
# print(s1.color)
# s1.start()

#multiple 
# class A:
#     var1="welcome to class A"
# class B:
#     var2="welcome to class B"
# class C(A,B):
#     var3="welcome to class C"
# s1=C()
# print(s1.var1)
# print(s1.var2)
# print(s1.var3)

#super method
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped..")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type,brand):
#         super().__init__(brand)
#         self.type=type

# s1=Fortuner("ev","prius")
# s1.start()
# print(s1.brand)
# print(s1.type)

#for change the class att name 
# class Person:
#     name = "xyz"
#     def change_name(self,name):
#         self.name = name 
# s1=Person()
# s1.change_name("falsi")
# print(s1.name)
# print(Person.name)    #in that both are diff so we change the method 

# class Person:
#     name = "xyz"
#     def change_name(self,name):
#         Person.name = name   #change the direct with class name
# s1=Person()
# s1.change_name("falsi")
# print(s1.name)
# print(Person.name) 

# class Person:
#     name = "xyz"
#     def change_name(self,name):
#         self.__class__.name = "falsi"    #__.class__. 
# s1=Person()
# s1.change_name("falsi")
# print(s1.name)
# print(Person.name) 

# class Person:
#     name = "xyz"
#     @classmethod
#     def change_name(cls,name):
#         cls.name=name 
# s1=Person()
# s1.change_name("falsi")
# print(s1.name)
# print(Person.name) 

#property decorator
# class Student: 
#     def __init__(self,phy,che,maths):
#         self.phy=phy
#         self.che=che
#         self.maths=maths

#     @property
#     def percentage(self):
#         return str((self.phy+self.che+self.maths)/3) +"%"
    
# s1=Student(99,98,96)
# print(s1.percentage)
# s1.che=88
# print(s1.percentage)


#complex number
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def show(self):
#         print(self.real, "i +" , self.img , "j")

# s1=Complex(1,3)
# s1.show()
# s2=Complex(3,4)
# s2.show()

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def show(self):
#         print(self.real, "i +" , self.img , "j")

#     def __add__(self,s2):
#         newReal = self.real + s2.real
#         newImg = self.img + s2.img
#         return Complex(newReal,newImg)
    
#     def __sub__(self,s2):
#         newReal = self.real - s2.real
#         newImg = self.img - s2.img
#         return Complex(newReal,newImg)

# s1=Complex(1,3)
# s1.show()
# s2=Complex(3,4)
# s2.show()
# res = s1+s2
# res.show()
# res2 = s1-s2
# res2.show()


#practice
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius*self.radius
    
#     def parimeter(self):
#         return 2*3.14*self.radius

# s1=Circle(10)
# print(s1.area())
# print(s1.parimeter())


# class Employee:
#     def __init__(self,role,dep,salary):
#         self.role=role
#         self.dep=dep
#         self.salary=salary
#     def showDetails(self):
#         print("role:",self.role)
#         print("department:",self.dep)
#         print("salary:",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age   
#         super().__init__("engineer","it","10000")

# s1=Engineer("falsi",20)
# s1.showDetails()


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,o2):
        return self.price>o2.price

o1=Order("chips",20)
o2=Order("tea",80)
print(o1>o2)
