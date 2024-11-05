import random

size = random.randint(5, 10)
s = []

for k in range(size):
    while True:
        if random.choice([True, False]):
            n = round(random.uniform(-10, 10), 2)
        else:
            n = random.randint(-10, 10)
        if n not in s:
            s.append(n)
            break

if not all(isinstance(num, (int, float)) for num in s):
    print("Список содержит некорректные данные:", n)

elif not s:
    print("Список пуст.")

elif len(s) == 1:
    print("Список содержит только один элемент:", n)

elif len(set(s)) != len(s):
    print("Список содержит дубликаты:", s)

elif len(set(s)) == 1:
    print("Все элементы списка одинаковы:", s)

else:
    min = s.index(min(s))
    max = s.index(max(s))

    print("Исходный список:", s)
    minn = s[min]
    maxn = s[max]
    s[min] = maxn
    s[max] = minn

    print("Измененный список, после замены максимального элемента на минимальный и минимального на максимальный: ", s)
