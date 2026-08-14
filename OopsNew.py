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




class Car:
    # maxSpeed = 150
    __maxSpeed = 150    # private variable / private Attribute : Can't update/edit outside class
    def __init__(self,name,fuelType):
        self.carName = name
        self.Fuel = fuelType

    def Start(self):
        print("Car engine is Started ... Enjoy your Drive")
    def MaximumSpeed(self):
        # print(f"Your Car Reached maximum speed : {self.maxSpeed}")
        print(f"Your Car Reached maximum speed : {self.__maxSpeed}")
    def Stop(self):
        print("Car engine Stopped , Hope you enjoy the Drive")

car1 = Car("Tata Harrier","Ev")
car2 = Car("BMW M4","Petrol")

# car1.Start()
# car1.MaximumSpeed()
# car1.Stop()

car2.Start()
# car2.maxSpeed = 220
car2.__maxSpeed = 200
car2.MaximumSpeed()
car2.Stop()