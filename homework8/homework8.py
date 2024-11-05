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
    print("Введите по одному числу из каждой строки лотерейного билета:")

    for i, row in enumerate(ticket):
        while True:
            try:
                num = int(input(f"Введите число из строки {i + 1} {row}: "))
                if num in row:
                    user_ticket.append(num)
                    break
                else:
                    print("Ошибка: число не найдено в строке. Попробуйте еще раз.")
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
print(f"Количество совпадений: {len(matches)}")
print(f"Совпадения: {matches}")
