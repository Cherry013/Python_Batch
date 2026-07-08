# class Employee:
#     bonus_rate = 0.1
#     def __init__(self,name,salary):
#         self.name = name
#         self.base_salary = salary
#
#     def final_salary(self):
#         return self.base_salary+(self.base_salary*Employee.bonus_rate)
#
#     @classmethod
#     def update_bonus(cls,nb):
#         cls.bonus_rate = nb
#
#     @staticmethod
#     def valid(sal):
#         return sal > 0

# e1 = Employee("Amarnath", 5000000)
# e2 = Employee("Shiva", 5000001)
#
# print(e1.final_salary())
# print(e2.final_salary())
# e1.update_bonus(0.2)
# print(e1.final_salary())
# print(e2.final_salary())

class Book:
    total_books = 0
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        t,a = book_str.split("-")
        if cls.is_valid(t):
            return cls(t,a)
        else:
            return "Invalid book string"

    @staticmethod
    def is_valid(t):
        return len(t) >= 3


# bts = "Harry Potter - J.K.Rowling"
# b1 = Book.from_string(bts)
# b2 = Book("The song of Ice and Fire","R.R.Martin")


class Inventory:
    total = 0
    threshold = 20
    def __init__(self):
        self.stock = {}

    def display(self):
        print(f"Inventory: {self.stock}")
        print(f"Total Stock: {self.total}")
        print(f"Minimum Stock: {self.threshold}")

    def add_item(self,item,quantity):
        if self.valid(quantity):
            self.stock[item] = quantity
            Inventory.total += 1
        else:
            print(f"quantity should be greater")
        self.display()

    def remove_item(self,item):
        if item in self.stock.keys():
            self.stock.pop(item)
            Inventory.total -= 1
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} not in inventory.")
        self.display()

    @classmethod
    def update(cls,nt):
        cls.threshold = nt

    @staticmethod
    def valid(qn):
        return qn >= Inventory.threshold

i1 = Inventory()
i2 = Inventory()
i3 = Inventory()
i1.add_item("'marker",90)
i2.add_item("mobile",25)
i3.add_item("laptop",15)
Inventory.update(10)
i3.add_item("laptop",15)
i1.remove_item('laptop')
i2.remove_item('mobile')



class Employee:
    minimum_exp = 5
    def __init__(self,name,exp,dept):
        if self.valid(dept):
            self.name = name
            self.exp = exp
            self.dept = dept
        else:
            print("Employee is not in the right Department")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Exp: {self.exp}")
        print(f"Department: {self.dept}")
        print('\n')

    def promotion(self):
        self.display()
        if self.exp >= Employee.minimum_exp:
            print("Eligible for promotion")
        else:
            print("Not Eligible for promotion")

    @classmethod
    def change(cls,mp):
        cls.minimum_exp = mp

    @staticmethod
    def valid(dep):
        l = ['HR','Tech','Admin','Non-Tech','Sales','Customer Service']
        return dep in l

e1 = Employee("Shiva",0,'Tech')
e2 = Employee("Pranitha",10,'HR')
e3 = Employee("Bhrammi",40,'Customer Service')
e4 = Employee('Pooja',20,'Admin')

e1.display()
e2.display()
e3.display()
e4.display()

e2.promotion()
e3.change(20)
e2.promotion()

















