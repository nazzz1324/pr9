import random

size = random.randint(5, 15)
s = []

for k in range(size):
    if random.choice([True, False]):
        n = round(random.uniform(-10, 10), 2)
    else:
        n = random.randint(-10, 10)
    s.append(n)

res = []
for i in range(1, size):
    if s[i] > s[i - 1]:
        res.append(s[i])

print("Исходный список:", s)
print("Элементы, которые больше предыдущего:", res)
