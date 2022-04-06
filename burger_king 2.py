def decor(bread):
    def wrapper():
        print("</------------\\>")
        bread()
        print("<\\____________/>")
    return wrapper


def bread():
    print('      булка')


br = decor(bread)


def decor(tomato):
    def wrapper():
        print("      ****")
        tomato()
        print("      ****")
    return wrapper


def tomato():
    print('    помидоры')


t = decor(tomato)


def decor(salad):
    def wrapper():
        print("      ~~~~")
        salad()
        print("      ~~~~")
    return wrapper


def salad():
    print('      салат')


s = decor(salad)


def decor(cheese):
    def wrapper():
        print("      ^^^^^^")
        cheese()
        print("      ^^^^^^")

    return wrapper


def cheese():
    print('       сыр')


ch = decor(cheese)


def decor(onion):
    def wrapper():
        print("     ------")
        onion()
        print("     ------")

    return wrapper


def onion():
    print('       лук')


o = decor(onion)


def decor(beef):
    def wrapper():
        print("       ###")
        beef()
        print("       ###")

    return wrapper


def beef():
    print('    говядина')


be = decor(beef)


def decor(chicken):
    def wrapper():
        print("      ||||")
        chicken()
        print("      ||||")

    return wrapper


def chicken():
    print('     Курица')


chi = decor(chicken)


br()
ch()
s()
chi()
br()
input()