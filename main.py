from abc import ABC, abstractmethod
import copy


class Item(ABC):
    @abstractmethod
    def get_summary(self):
        pass

class Book(Item):
    catlog_tag = []
    def __init__(self,title:str,avail:bool,price:int):
        self.title = title
        self.__metadata = {}
        self._availability = avail
        self.price = price

    @property
    def metadata(self):
        return copy.deepcopy(self.__metadata)
    @property
    def scopy(self):
        return self.__metadata

    @classmethod
    def update(cls,n):
        cls.catlog_tag.append(n)

    def pricing(self,discount:float=0):
        price = self.price
        if discount:
            price -= (price * discount)
        return price

    def get_summary(self):
        print("Just a Summary")

    def __str__(self):
        return f"{self.title} : {'available' if self._availability else 'not available'} \nPrice: ₹{self.price}"
    def __repr__(self):
        return f"{self.title} : {'available' if self._availability else 'not available'} \nPrice: ₹{self.price}"

    @staticmethod
    def validator(k):
        return "Valid" if isinstance(k,(str,tuple,int,)) else "Invalid"


# b1 = Book("The Author's Pov",True,399)
# print(b1)
# b1.update("brought by 3")
# print(b1.pricing())
# k = b1.metadata
# l = b1.scopy
# k["hello"] = "world"
# print(b1.metadata)



class UserBase(ABC):
    @abstractmethod
    def get_role(self):
        pass

class Member(UserBase):
    user_count = 0
    admin_flag = False
    permission = ["write","read","execute","update","delete","upgrade","degrade"]

    def __init__(self,username,credentials):
        self.username = username
        self._credentials = credentials
        self.__perms = []
        Member.user_count += 1

    @property
    def permissions(self):
        return copy.deepcopy(self.__perms)

    @property
    def cred(self):
        return "*******"

    def get_role(self):
        pass

    def perform(self,action,timeout=3):
        pass

    @staticmethod
    def valid(p:str):
        return p.lower() in Member.permission

    def __add__(self,o2):
        if o2 not in self.__perms:
            self.__perms.append(o2)
        return self

    def __sub__(self,o2):
        if o2 not in self.__perms:
            print("Permission denied")
            return self
        self.__perms.remove(o2)
        return self

    def __eq__(self, other):
        return self.username == other.username and self.permissions == other.permissions

    def __str__(self):
        return f"{self.cred}"
    def __repr__(self):
        return f"{self.username} : {self.permissions}"

#
# u1 = Member("Balaji","Balaji2001")
# u2 = Member("Dheeraj","12345678")
# u1 + "write" + "read"
# u2 + "write" + "read" + "execute"
# u1 - "write"
# print(u1.permissions)
# print(u2.permissions)
# print(u1 == u2)
# print(u1)
# print(u2)



# def dec(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         count+=1
#         print(count)
#         func()
#     return wrapper
#
# @dec
# def fun():
#     print("hello")

# fun()
# fun()
# fun()
# fun()



def fun():
    x=30
    def fun2():
        print(x)
    return fun2

# k = fun()
# print(k)
# print(k.__name__)
# print(k.__closure__)
# print(k.__closure__[0].cell_contents)
# k()
# k.__closure__[0].cell_contents = 50
# k()


#
# def dec(func):
#     def inner():
#         pass
#     return inner
#
#
#
# @dec # fun = dec(fun)
# def fun():
#     print("World Hello")
#
# fun()


# def fun(x):
#     def fun2():
#         print(x)
#         print(x.__name__)
#         x()
#     return fun2

# k = fun(fun3)
# k()
# print(k.__name__)
# @fun
# def fun3():
#     print("World Hello")
# fun3 = fun(fun3)
# fun3()

def dec(func):
    def inner(n):
        print("Starting this Function")
        print(func.__name__)
        func(n)
        print("ending this Function")
    return inner

@dec # greet = dec(greet)
def greet(name):
    print(f"Hello {name}")
#
# print(greet.__name__)
# greet("Nikhil")








def valid(func):
    def inner(x,y):
        if isinstance(x,int) and isinstance(y,int):
            print(f"Multiplication of {x} & {y}:",end=" ")
            func(x,y)
        else:
            print("Values/Arguments Must be Integers")
    return inner

@valid
def multiply(x,y):
    print(x*y)

multiply(4,5)
multiply('4',5)


def login(func):
    def inner():
        un = input("Username: ")
        psd = input("Password: ")
        if un == "praveen" and psd == "Diya":
            print("Login Successful")
            return func()
        else:
            return "Invalid Credentials"

    return inner


@login
def securefile():
    return "Secret File"

print(securefile())

















