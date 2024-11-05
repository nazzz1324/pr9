import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]


def get_ticket():
    user_ticket = []
    user_rows = set()
    print("Введите 5 чисел (по одному из каждой строки лотерейного билета):")

    for _ in range(5):
        while True:
            try:
                num = int(input(f"Введите число: "))
                row_index = None
                for i, row in enumerate(ticket):
                    if num in row:
                        row_index = i
                        break

                if row_index is None:
                    print("Ошибка: число не найдено в билетах. Попробуйте ещё раз.")
                elif row_index in user_rows:
                    print("Ошибка: выбрано более одного числа из одной строки. Попробуйте ещё раз.")
                else:
                    user_ticket.append(num)
                    user_rows.add(row_index)
                    break
            except ValueError:
                print("Ошибка: введите корректное число.")

    return user_ticket


def generate_ticket():
    random_ticket = [random.choice(row) for row in ticket]
    return random_ticket

user_ticket = get_ticket()

random_ticket = generate_ticket()

print(f"\nВаш лотерейный билет: {user_ticket}")
print(f"Случайно сгенерированный билет: {random_ticket}")


matches = set(user_ticket) & set(random_ticket)
result = ', '.join(str(item) for item in matches)
print(f"Количество совпадений: {len(matches)}")
print(f"Совпадения: {result}")
