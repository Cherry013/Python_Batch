def fun(a:int, b:int) -> int:
    """Just Experimenting with functions"""
    return a*b

# print(f"Name : {fun.__name__}")
# print(f"Document : {fun.__doc__}")
# print(f"Class : {fun.__class__}")
# print(f"Class Name : {fun.__class__.__name__}")
# print(f"Class Doc : {fun.__class__.__doc__}")
# print(f"Class Module : {fun.__class__.__module__}")
# print(f"Just seeing what it is : {fun.__type_params__}")



class User:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

class Student(User):
    __PFS = 0
    def __init__(self, name:str, age:int, course:int, subject=None):
        # if isinstance(self, Student):
        #     super().__init__(name, age)
        # else:
        super().__init__(name, age, subject)
        if course == "PFS":
            Student.__PFS += 1
        self.course = course

    @property
    def score(self):
        return Student.__PFS

    def submit_work(self):
        print("Completed Work")




class Instructor(User):
    def __init__(self, name:str, age:int, subject:str):
        super().__init__(name, age)
        if subject:
            self.subject = subject

    def grade_work(self):
        print("Grading Completed")


class TeachingAssistant(Student, Instructor):
    def __init__(self, name:str, age:int, course:str, subject:str):
        super().__init__(name, age, course, subject)

    def submit_work(self):
        print("Overriding the method")

    def grade_work(self):
        print("Overriding the Grade method")

#
# print(TeachingAssistant.mro())
# print(Student.mro())
# print(Instructor.mro())
#
# ta = TeachingAssistant("Nithin",60,"python Full stack", "cross over")
# print(ta.course,ta.subject, ta.name,ta.age)
# print(Student.mro())
# print(Instructor.mro())



class Product:
    def __init__(self, name, Price, Quantity):
        self.name = name
        self.__Price = Price
        self.__Quantity = Quantity

    def __str__(self):
        return f"{self.name} : {self.__Quantity}"

    def __repr__(self):
        return f"{self.name} : {self.__Quantity}"

class Warehouse:
    total = 0
    def __init__(self):
        self.inv = []
        Warehouse.total += 1

    def add(self,product:Product):
        self.inv.append(product)

    def remove(self,product:Product):
        if product in self.inv:
            self.inv.remove(product)
        else:
            print("Product not in the list")
    @classmethod
    def track(cls):
        print(f"Total Warehouses : {Warehouse.total}")

    def __add__(self, other):
        return self.inv + other.inv

    def __len__(self):
        return len(set(self.inv))

    def __contains__(self, item):
        return item in self.inv
p1 = Product("Milk",50, 25)
p2 = Product("Chacolate", 60, 20)
p3 = Product("Book", 70, 10)


# w1 = Warehouse()
# w1.add(p1)
# w1.add(p2)
# w1.add(p3)
# w1.add(p1)
# w1.add(p2)
# w2 = Warehouse()
# w2.add(p1)
# w2.add(p2)
# print(w1+w2)
# print(len(w1))
# print(p3 in w2)
# print(p2 in w1)

from abc import ABC, abstractmethod
class MediaFile(ABC):
    def __init__(self, path:str):
        self.__path = path

    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass

    @staticmethod
    def validation(path):
        return "/media" in path


class Mp3File(MediaFile):
    def play(self):
        print("Playing Mp3")

    def stop(self):
        print("Stopping Mp3")

class Mp4File(MediaFile):
    def play(self):
        print("Playing Mp4")

    def stop(self):
        print("Stopping Mp4")

class WavFile(MediaFile):
    def play(self):
        print("Playing Wav")

    def stop(self):
        print("Stopping Wav")

def start_player(media:MediaFile):
    media.play()
    media.stop()


# l = [Mp3File("/media/oye oye.mp3"), Mp4File("/media/Bhahubali.mp4"), WavFile("/Wav/just a file.wav")]
# for i in l:
#     start_player(i)








class Loan:
    interest_rate = 0.05
    def __init__(self, name, principal):
        self.name = name
        self.principal = principal

    def total_amount(self):
        return self.principal + (self.principal * self.interest_rate)

    @classmethod
    def update(cls,ni):
        cls.interest_rate = ni


    @staticmethod
    def valid(sal):
        return sal>50000

# l1 = Loan("Milk", 10000)
# l2 = Loan("Chacolate", 200000)
# print(l1.total_amount())
# print(l2.total_amount())
# l1.update(0.1)
# print(l1.total_amount())


class Inventory:
    total_items = 0
    threshold = 30
    def __init__(self):
        self.stock = {}

    def add_item(self, item, quantity):
        if item not in self.stock.keys():
            if self.valid(quantity):
                self.stock[item] = quantity
                Inventory.total_items += 1
                print(f"Added {item} to inventory {Inventory.total_items}")
            else:
                print("Quantity is less")
        else:
            self.stock[item] += quantity
            print(f"Quatity updated {item} to {quantity}")

    def remove_item(self, item):
        if item in self.stock.keys():
            self.stock.pop(item)
            Inventory.total_items -= 1
        else:
            print("Item not in inventory")

    @classmethod
    def update(cls,ni):
        cls.threshold = ni

    @staticmethod
    def valid(quantity):
        return quantity >= Inventory.threshold


# i1 = Inventory()
# i2 = Inventory()
#
# print(i1.stock)
# print(i2.stock)
#
# i1.add_item("Milk", 30)
# i1.add_item("Chacolate", 20)
# i2.add_item("Book", 100)
# i2.add_item("Milk", 50)
# i1.add_item("Marker", 70)
# i1.add_item("Milk", 50)
# Inventory.update(20)






class A:
    x = None
    def __new__(cls, *args, **kwargs):
        # return super().__new__(cls)
        if cls.x is None:
            cls.x = super().__new__(cls)
        return cls.x

    def __init__(self,name):
        self.name = name
    # def __str__(self):
    #     return f"Name: {self.name}"
    def __repr__(self):
        return self.name

# a1 = A("Aliya")
# a2 = A("Bhoomi")
# a3 = A("Lokesh")
#
# print(a1)
# print(a2)
# print(a3)



class Co_ordinates:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Co_ordinates(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self,other):
        return other + self

    def __sub__(self,other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self,other):
        return (self.x * other.x, self.y * other.y, self.z * other.z)

    def __floordiv__(self,other):
        return (self.x // other.x, self.y // other.y, self.z // other.z)

    def __mod__(self,other):
        return (self.x % other.x, self.y % other.y, self.z % other.z)

    def __str__(self):
        return f"Co_ordinates({self.x}, {self.y}, {self.z})"


c1 = Co_ordinates(1,2,3)
c2 = Co_ordinates(4,5,6)
c3 = Co_ordinates(7,8,9)
#
# print(c1+c2) # c1.__add__(c2)
# # c2.__radd__(c1)
# print(type(c1+c2))
# print(c1 - c2)
# print(c1*c2)
# print(c1//c2)
#
# print(c1+c2+c3)



class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __sub__(self,o2):
        return Vector(self.x - o2.x, self.y - o2.y)

    def __mul__(self,other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self,other):
        return Vector(self.x / other.x, self.y / other.y)

    def __mod__(self,other):
        return Vector(self.x % other.x, self.y % other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(5,6)
v2 = Vector(9,10)
v3 = Vector(3,4)
#
# v = [v1,v2,v3]
# print(v)
# print(v1+v2+v3) # v1.__add__(v2) --> Vector.__add__(v1,v2)
# print(type(v1+v2))
# print(v1-v2)
# print(v1*v2)
# print(v1/v2)
# print(v1%v2)


class Inventory:
    total_items = 0
    def __init__(self):
        self.stock = {}


i1 = Inventory()
i2 = Inventory()
i1+"Marker"+"Mobile"
i2+"TV"+"Laptop"
print(i1)
print(i2)
print(i1-"Laptop")
print(i2-"TV")

