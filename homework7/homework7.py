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
    print("Список элементов до сдвига каждого элемента вправо: ", s)

    if len(s) > 1:
        last = s[-1]
        for i in range(len(s) - 1, 0, -1):
            s[i] = s[i - 1]
        s[0] = last

    print("Список элементов после сдвига каждого элемента вправо: ", s)

