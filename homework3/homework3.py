s = []

while True:
    try:
        a = input("Введите целые число либо 'end' для завершения ввода: ")
        if a == 'end':
            break
        s.append(int(a))

    except ValueError:
        print("Ошибка: пожалуйста, введите корректные целые числа.")

uneven = []

for i in range(0, len(s)):
    if s[i] % 2 != 0:
        uneven.append(s[i])

result = ', '.join(str(item) for item in uneven)

print(f'Нечетные числа среди введенных: {result} ')

