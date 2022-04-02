numbers = [int(s) for s in input("Введите числа через пробел - ").split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)