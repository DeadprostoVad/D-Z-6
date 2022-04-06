n = int(input("Введите число = "))

def sum(n):
    if n < 10:
        return n
    else:
        return sum(n // 10) + n % 10

print(sum(n))


