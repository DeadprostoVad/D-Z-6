def bread(funct):
    def wrapper():
        print("</------------\\>")
        funct()
        print("<\\____________/>")
    return wrapper


def tomato(funct):
    def wrapper():
        print("***" f'помидоры' "****")
        funct()
    return wrapper


def salad(decor):
    def wrapper():
        print("~~~~" f'салат' "~~~~~")
        decor()
    return wrapper

def cheese(funct):
    def wrapper():
        print("^^^^^" f'сыр' "^^^^^^")
        funct()
    return wrapper

def onion(funct):
    def wrapper():
        print("-----" f'лук' "------")
        funct()
    return wrapper


def chicken(funct):
    def wrapper():
        print("||||" f'курица' "||||")
        funct()
    return wrapper


def beef(funct):
    def wrapper():
        print("###" f'говядина' "###")
        funct()
    return wrapper()


@bread
@onion
@tomato
def beef():
    print("###" f'Говядина' "###")



@bread
@cheese
@salad
def chicken():
    print("||||" f'курица' "||||")


print("Гамбургер")
beef()
print("\n \n")
print("Чикенбургер")
chicken()

