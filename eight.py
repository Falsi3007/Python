# class Student:
#     name = "falsi"
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)

# class car:
#     name = "Mercedes"
#     color = "black"
# car1 = car()
# print(car1.name)
# print(car1.color)

# class Student:
#     college_name = "charusat"
#     #default constructor
#     def __init__(self):
#         pass
#     #parameterized constructor
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
# s1 = Student("falsi",98)
# print(s1.name,s1.marks,s1.college_name)
# s2 = Student("karan",99)
# print(s2.name,s2.marks,s2.college_name)

# class Student():
#     name = "anonymous"  #class att
#     def __init__(self,name):
#         self.name=name     #obj.att>class.att
# s1=Student("falsi")
# print(s1.name)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name 
#         self.marks=marks
#     def welcome(self):
#         print("welcome",self.name)
#     def get_marks(self):
#         return self.marks
# s1=Student("falsi",88)
# s1.welcome()
# print(s1.get_marks())

# class Student:
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"avg score",sum/3)
# s1=Student("falsi",[95,93,90])     
# s1.get_avg()


#abstraction
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("car started")
# s1=Car()
# s1.start()


#practice 
# class Account:
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no=acc_no

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.", amount , "was debited.")
#         print("total balance = ",self.get_balance())

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs." ,amount ,"was credited.")
#         print("total balance = ",self.get_balance())


#     def get_balance(self):
#         return self.balance

# s1 = Account(1000,1)
# print(s1.acc_no,s1.balance)
# s1.debit(100)
# s1.credit(200)
# s1.get_balance()
