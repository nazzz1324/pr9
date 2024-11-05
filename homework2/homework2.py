def get_square_list(a, b):

    start = int(min(a, b))
    end = int(max(a, b))

    numbers = [i for i in range(start, end + 1) if (i > a and i < b) or (i < a and i > b)]

    squares = [i ** 2 for i in numbers]

    return numbers, squares

while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        break
    except ValueError:
        print("Ошибка: пожалуйста, введите корректные числа.")

numbers, squares = get_square_list(a, b)

print(f"Целые числа в диапозоне [{a};{b}]: {numbers}")
print(f"Квадраты целых чисел: {squares}")

