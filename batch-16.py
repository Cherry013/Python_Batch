def adding(x:str,y:str) -> str:
    return x+y

# list, tuple, str, dict, int, float, bool

# print(adding("asd","asd"))
# print(adding.__annotations__)

def add(x,y):
    return x+y
# print(add.__name__)
# print(add)

# a = add
# print(add(10,20))
# print(a(10,20))

def fun4():
    def fun5():
        print("Hello")
    return fun5

# fun = fun4() # fun = fun5
# fun()

def fun6():
    def inner(name):
        print(f"Hello {name}")
    return inner
#
# l = fun6()
# l("Prabhas")


def dec(x):
    def inner(y):
        print(x+y)
        return y
    return inner

# k = dec(50)
# print(k(30))
# print(k.__closure__)
# print(k.__closure__[0].cell_contents)
# k.__closure__[0].cell_contents = 100
# print(k.__closure__[0].cell_contents)
# print(k(30))


def validation(func):
    def inner(*args):
        # print(args)
        # l = []
        # for i in args:
        #     if isinstance(i,int):
        #         l.append(i)
        # l = tuple(l)

        l = tuple(filter(lambda x: isinstance(x,int),args))
        return func(*l)

    return inner

@validation
def just(*args):
    print(f"args: {args}")
    return sum(args)

# print(just(1,2,3,'66',[45],123,'78'))

def password_validator(func):
    def inner(psd:str):
        sp = ['@','*','!','#','$','%','&','_','-','=','+','/']
        if len(psd)>=8:
            up = list(filter(lambda x: x.isupper(),psd))
            sc = list(filter(lambda x:x in sp, psd))
            dg = list(filter(lambda x: x.isdigit(),psd))

            print(up,sc,dg,sep='\n')

            if up and sc and dg:
                print("Strong Password")
                func(psd)
            else:
                print("Weak Password")
        else:
            print("password must contain 8 characters")
    return inner

@password_validator
def password(ps):
    print(f"password {ps} is accepted")


password("23456fghbnkH")
password("765FHGDk#$")


@register
def registration(us,psd,age):
    pass



