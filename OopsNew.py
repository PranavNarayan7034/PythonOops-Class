# OOPS (Object oriented programming)
# a programming approach where we organize a program around objects 
# and classes rather than only functions and procedures.

# Object:   A data with properties 

# Car : data 
# car1 : {color:"Red",Brand:"Tata",Fuel:"Ev",Mileage:25,SeatCapactiy:5}  : object
# car2 : {color:white,Brand:"Bmw",Fuel:"petrol",Mileage:13,SeatCapactiy:7}

# car1.color = "red", car1.Brand = "Tata" , car1.Fuel = 'Ev', car1.Mileage = 25 ......
# car2.color = "White" , car2.Brand = 'Bmw', car2.Fuel = "Petrol" , car2.Mileage = 13 .....

# stud1 : {studid:10,Name:"Sam",Age:22,subject:"Mechanical"}  : object 

# class : A blue print to create object 
# methods : functions that defined inside class 
# attributes : variables that declared inside class 

# def show():
#     print("Python Function is calling")

# class Employee:
#     def display(self):         # method
#         print("Welcome to oops Concept")

# emp1 = Employee()    # object / instance of class
# emp2 = Employee()    # object / instance of class
# emp3 = Employee()    # object / instance of class
# emp4 = "object"

# # print(emp1)
# # print(emp2)
# # print(emp3)

# show()
# # display()   Error
# emp1.display()
# emp3.display()



# class car:
#               # car1, "red","Tata","Ev",25,5
#     def __init__(self,clr,brnd,fuel,mileage,seats):  # 1. self = car1   , 2. self = car2 ,3. self=car3
#         self.Color = clr    # car1.Color = red
#         self.Brand = brnd   # car1.Brand = Tata
#         self.Fuel = fuel         # car1.Fuel = Ev
#         self.Mileage = mileage
#         self.Seats = seats

# car1 = car("Red","Tata","Ev",25,5)
# car2 = car("White","BMW","Petrol",13,7)
# car3 = car("Grey","Suzuki","Diesel",22,5)

# print(car1)
# print(car2)

# print(car1.__dict__)
# print(car3.__dict__)

# **********************************************************************
# class Employee:
#     def __init__(self,id,name,sal,dept,exp):
#         self.Empid = id
#         self.EmpName = name
#         self.Salary = sal
#         self.Dept = dept
#         self.Exp = exp
# #     def SalaryIncrement(self):  
# #         print("Incremented salary after 10% Addition :",round(self.Salary*1.10))

# emp1 = Employee("Emp454545","Manu",56000,"IT",2)
# emp2 = Employee("Emp784555","Sera",58900,"Developer",2)
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(emp1.Salary)
# print(emp2.Salary)

# emp1.SalaryIncrement()
# emp2.SalaryIncrement()

# print(round(45445.45564656484,3))
# print(round(45445.45564656484))
# ****************************************************************


# class Employee:
#     percentage = 1.10    # attribute
#     def __init__(self,id,name,sal,dept,exp):
#         self.Empid = id
#         self.EmpName = name
#         self.Salary = sal
#         self.Dept = dept
#         self.Exp = exp
#     def SalaryIncrement(self):     # self = emp1
#         print("Incrementation = ", self.percentage)
#         print("New salary =", round(self.Salary * self.percentage))
#         print("**************")

# emp1 = Employee("Emp454545","Manu",56000,"IT",2)
# emp2 = Employee("Emp784555","Sera",58900,"Developer",2)
# emp3 = Employee("Emp755455","Jacob",75425,"TL",5)

# emp1.percentage = 1.05
# emp1.SalaryIncrement()
# emp2.SalaryIncrement()

# emp3.percentage = 1.15
# emp3.SalaryIncrement()




# Q: Create a class with products having properties 
# product_id
# product_name
# product_brand
# product_price
# Remaining_Qty
# >> based on this properties create 3 object . 

# ** We are planning to give 5% discount of price of each products 
# ** if product remaining qty is more than 25 give discount as 15 % 
# ** print each product new price

# class Product:
#     def __init__(self,id,name,brand,price,qty):
#         self.productId = id
#         self.productName = name
#         self.productBrand = brand
#         self.productPrice = price
#         self.remaining_qty = qty

#     def discountPrice(self):
#         if self.remaining_qty > 25:
#             print(f'Your product 15% discount . New price = {self.productPrice * 0.85}')
#         else:
#             print(f'Your product 5% discount . New price = {self.productPrice * 0.95}')

# prd1 = Product(101,"Laptop","HP",76999,15)
# prd2 = Product(102,"Headphone","JBL",7999,28)
# prd3 = Product(103,"Mouse","Zebronics",1599,20)

# print(prd1.__dict__)
# print(prd1.productPrice)
# print(prd1.remaining_qty)
# print(prd2.productPrice)
# print(prd2.remaining_qty)

# print(prd1.__dict__)
# print(prd1.productPrice)
# prd1.discountPrice()

# print(prd2.productPrice)
# prd2.discountPrice()


# Encapsulation 

# class Car:
    # maxSpeed = 150
    # __maxSpeed = 150    # private variable / private Attributes : Can't update/edit outside class
    # def __init__(self,name,fuelType):
    #     self.carName = name
    #     self.Fuel = fuelType

    # def Start(self):
    #     print("Car engine is Started ... Enjoy your Drive")
    # def MaximumSpeed(self):
    #     # print(f"Your Car Reached maximum speed : {self.maxSpeed}")
    #     print(f"Your Car Reached maximum speed : {self.__maxSpeed}")
    # def Stop(self):
    #     print("Car engine Stopped , Hope you enjoy the Drive")

# car1 = Car("Tata Harrier","Ev")
# car2 = Car("BMW M4","Petrol")

# car1.Start()
# car1.MaximumSpeed()
# car1.Stop()

# car2.Start()
# car2.maxSpeed = 220
# car2.__maxSpeed = 200
# car2.MaximumSpeed()
# car2.Stop()

# private Methods 


# class Employee:
#     def __init__(self,id,fname,lname,salary):
#         self.id = id
#         self.FirstName = fname
#         self.LastName = lname 
#         self.Salary = salary
#         # self.Email = self.GenerateEmail()
#         self.Email = self.__GenerateEmail()

#     def GenerateEmail(self):
#         # print(f'{self.FirstName}{self.LastName}{self.id}@companymail.com')
#         return f'{self.FirstName}{self.LastName}{self.id}@companymail.com'

#     def __GenerateEmail(self):      # private methods
#             # print(f'{self.FirstName}{self.LastName}{self.id}@companymail.com')
#             return f'{self.FirstName}{self.LastName}{self.id}@companymail.com'

# emp1 = Employee(55,"David","James",58900)
# emp2 = Employee(85,"Catherine","Teresa",78500)
# print(emp1.__dict__)
# emp1.GenerateEmail()
# print(emp2.__dict__)
# emp2.GenerateEmail()

# print(emp1.__dict__)
# x = emp2.GenerateEmail()
# print(x)

# x = emp2.__GenerateEmail()
# print(x)



# Inheritance 

# class Employee:
#     def Display(self):
#         print("Display fn executed in Employee Class")

# class Developer:
#     def Show(self):
#         print("Show fn executed inside Developer class")

# h1 = Employee()
# h2 = Developer() 

# h2.Display()  # Error
# h1.Display()
# h2.Show()
# h1.Show()    # Error 

# *************************************************


class Employee:
    def Display(self):
        print("Display fn executed in Employee Class")

class Developer(Employee):     
    # inheritance : Inheriting one class properties 
    # in to another
    # Developer = child class 
    # Employee = parent class / super class 
    def Show(self):
        print("Show fn executed inside Developer class")

# h1 = Employee()
h2 = Developer()

# h2.Show()
# h2.Display()

# h1.Show()

# ************************************************


# class Employee: 
#     def __init__(self,id,name,salary):
#         self.Empid = id 
#         self.Empname = name
#         self.Salary = salary

# class Developer(Employee):
#     def __init__(self,id,name,salary,Lang,Projects):
#         super().__init__(id,name,salary)
#         self.Languages = Lang 
#         self.completedProject = Projects

# class Tester(Employee):
#     def __init__(self,id,name,salary,tools):
#         super().__init__(id,name,salary)
#         self.Tools = tools

# class Support:
#     pass 

# per1 = Developer(1045,"Sera",56800,["Python","java" ,"c"] ,10) 
# per2 = Tester(1046,"Sanjith",42000,["Jira",'Selenium'])
# per3 = Support()

# print(per1.__dict__)
# print(per2.__dict__)

# Types of inheritance

# 1. single inheritance : 
# One child class inheriting from one pararent class

# class Employee:
#     def Display(self):
#         print("Display fn executed in Employee Class")

# class Developer(Employee):      
#     def Show(self):
#         print("Show fn executed inside Developer class")

# h2 = Developer() 
# h2.Show()
# h2.Display()








# 2. Multiple inhertiance 
# one child class inherits from multiple parent class 

# class Father:
#     def Skills(self):
#         print("Drawing")

# class Mother:
#     def Talent(self):
#         print("Singing")

# class Child(Mother,Father):
#     def info(self):
#         print("I am a child")

# p2 = Mother()
# p2.Talent()
# p2.info()
# p2.Skills()

# p1 = Child()
# p1.info()
# p1.Talent()
# p1.Skills()

# 3.Multi-level inheritance 

# class Grandparents:
#     def Car(self):
#         print("Grand parent's Car")

# class Parents(Grandparents):
#     def House(self):
#         print("Parent's House")

# class Child(Parents):
#     def Bike(self):
#         print("My bike")

# # h1 = Parents()
# # h1.House()
# # h1.Car()
# # h1.Bike()

# h2 = Child()
# h2.Bike()
# h2.House()
# h2.Car()

# 4.Hierarchilal inheritance 
# Multiple child classes inherit from one parent class 

# class Animal:
#     def Property(self):
#         print("They are Eating Food")

# class Dog(Animal):
#     def Bark(self):
#         print("Dog's are BARKING")

# class Cat(Animal):
#     def Meow(self):
#         print("Cat's are MEOWING")


# A1 = Cat()
# A1.Meow()
# A1.Property()
# A1.Bark()

# 5. Hybrid inheritance 


# Different types of methods 
# 1. Instance method / regular methods 
# Methods that works with object 

# class Student:
#     collegeName = "Abc College"
#     def __init__(self,name,age,main):
#         self.StudentName = name 
#         self.StudentAge = age 
#         self.MainSub = main 
#     def Display(self):
#         print(f"Display method is calling :, {self.StudentName}")

# s1 = Student("Rahul",23,"Mechanical")
# print(s1.__dict__)
# s1.Display()
# print(s1.collegeName)
# print(Student.collegeName)
# Student.Display()      # Error 









# 2. Class Methods 
# works with class, we can call class methods 
# using class rather than object 

# class Student:
#     collegeName = "Abc College"
#     def __init__(self,name,age,main):
#         self.StudentName = name 
#         self.StudentAge = age 
#         self.MainSub = main 
#     def Display(self):
#         print(f"Display method is calling :, {self.StudentName}")

#     @classmethod
#     def CollegeInfo(cls):    # cls = Student
#         print("This Class Method print your college info")
#         print(f"Your college Name = {cls.collegeName}")

# s1 = Student("Rahul",23,"Mechanical")
# Student.CollegeInfo()







# class Student:
#     collegeName = "Abc College"
#     TotalStudent = 350 
#     ParticipationFee = 100
#     def __init__(self,name,age,main):
#         self.StudentName = name 
#         self.StudentAge = age 
#         self.MainSub = main 
#     @classmethod
#     def updateFee(cls,Amount):      # cls = Student, Amount = 250
#         cls.ParticipationFee = Amount

# s1 = Student("Rahul",23,"Mechanical")
# s2 = Student("Mike",21,"Chemistry")
# s3 = Student("Sana",22,"Cs")

# s1.ParticipationFee = 200
# print(s1.ParticipationFee)
# print(s2.ParticipationFee)
# print(s3.ParticipationFee)
# print(Student.ParticipationFee)

# Student.updateFee(250)
# print(s1.ParticipationFee)
# print(s2.ParticipationFee)
# print(s3.ParticipationFee)


# Q: Create a class method find the total 
# Amount we got from student in Event 

# Student.TotalAmount()  ==> 350*100


# class Student:
#     collegeName = "Abc College"
#     TotalStudent = 350 
#     ParticipationFee = 100

#     def __init__(self,name,age,main):
#         self.StudentName = name 
#         self.StudentAge = age 
#         self.MainSub = main 

#     def displayStudentinfo(self):       # REGULAR METHOD / INSTANCE METHOD
#         print(f"Student name: {self.StudentName}, college = {self.collegeName}")

#     @classmethod                        # CLASS METHOD
#     def TotalAmount(cls):  # cls = Student
#         print(f"Total Amount collected from student side = {cls.TotalStudent * cls.ParticipationFee}")

# s1 = Student("Rahul",23,"Mechanical")
# s2 = Student("Mike",21,"Chemistry")
# s3 = Student("Sana",22,"Cs")

# Student.TotalAmount()



# static method: 
# methods that doesn't require any self/ cls attributes to execute fn 

# class Student:
#     college = "Abc College"
#     totalStudents = 350
#     def __init__(self,name,age,main):
#         self.StudentName = name 
#         self.StudentAge = age 
#         self.MainSub = main 

#     @staticmethod
#     def Cacluator(a,b):
#         return a + b

#     @staticmethod
#     def Info():
#         print("Welcome to Student class in python OOPS")

# s1 = Student("Rahul",23,"Mechanical")
# s2 = Student("Mike",21,"Chemistry")
# s3 = Student("Sana",22,"Cs")

# print(Student.Cacluator(10,50))
# Student.Info()


# Polymorphism : Means the same method can behave differently depending on object 

# class India: 
#     def Capital(self):
#         print("Capital of INDIA = NewDelhi")
# class England:
#     def Capital(self):
#         print("Capital of ENGLAND = London") 
# class UAE:
#     def Capital(self):
#         print("Capital of UAE = Abudabi")
# class Spain:
#     def Capital(self):
#         print("Capital of SPAIN = Madrid") 
# class France:
#     def Capital(self):
#         print("Capital of FRANCE = Paris")
# P1 = India()
# P2 = England()
# P3 = UAE()
# P4 = Spain()
# P5 = France()
# # P2.Capital()
# # P3.Capital()
# # P5.Capital()

# for i in (P1,P2,P3,P4,P5):
#     i.Capital()


# Abstract class
# ABC is a class that used as a  blueprint for other classes 

# from abc import ABC , abstractmethod 
# class Bank(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class CreditCard(Bank):
#     def __init__(self,cardno,name):
#         self.cardno = cardno
#         self.cardname = name
#     def pay(self):
#         print("Credit card payment is completed")

# class Onlinepayment(Bank):
#     def Info():
#         pass
#     def pay(self):
#         print("Online payment Completed")

# class DebitCard(Bank):
#     def pay(self):
#         print("Debit card payment is completed")

# p1 = CreditCard(45455645455,"Mike")
# p2 = Onlinepayment()
# p3 = DebitCard()
# print(p1.__dict__)


# Decorators in python 
# 1.first order fn 
# 2.higher order fn  
# 3.closure
# 4.decorators 

# 1. First order fns : we can store fn name into a variable, 
# and excute it while calling variable 

# def Cube(x):
#     return x**3 

# print(Cube(5))

# a = Cube(5)     # a = 125
# print(a)

# a = Cube          # a = Cube
# print(a)
# print(a(5))


# 2. Higher order fn : Takes another fn as argument and returns a another fn
# def add(x,y):
#     return x+y 
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y 
# def div(x,y):
#     return x/y
 
# def calculate(func,x,y):   
    # out = func(x,y)            # add(50,20)   , mul(10,30)
    # return out

    # return func(x,y)

# a = calculate(add,50,20) # func = add, x = 50 , y = 20
# print(a)
# b = calculate(mul,10,30) # func = mul, x = 10 , y = 30
# print(b)


# def square(x):
#     return x**2

# def cube(x):
#     return x**3

# def myMap(fn,list):    # fn = square, list = [10,20,30,40,35,25]
#     result = []     # result = [squre(10), square(20), square(30)...... square(25)]
#                     # result = [100,400,900,......]
#     for i in list:
#         result.append(fn(i))
#     return result

# s1 = myMap(square,[10,20,30,40,35,25])
# s2 = myMap(cube,[10,20,30,40,35,25])
# print(s1)  
# print(s2)  


# closure 
# Innerfn that are enclosed with in an outer fn
# closure can access variable inside outer fn 
# even though outer fn execution completed.

# def outerFn():
#     message = "Welcomet to Closure"
#     print("Outer fn executed")
#     def innerFn():
#         print("Inner fn executed")
#         print(message)

#     innerFn()
    
# outerFn()
# innerFn()   # error





# *********************************************

def outerFn():
    message = "Welcomet to Closure"
    print("Outer fn executed")
    def innerFn():
        print("Inner fn executed")
        print(message)

    return innerFn
    
a = outerFn()   # a = inner fn 
print(a)
# print("Variable a ==" ,a)
a()



