# Обчислюємо факторіал числа n за допомогою рекурсії
# @param n – число, для якого треба розрахувати факторіал
# @return - факторіал числа n
def factorial(n):
    print(f"Current n {n}")
    if n < 2:
        print(f"Base {n}")
        return 1  # Базовий випадок
    else:
        result = n * factorial(n - 1)  # Рекурсивний випадок
        print(f"Recursion {result}")
        return result


num = int(input("Введіть додатне ціле число: "))
result = factorial(num)
print(f"Факторіал числа {num} дорівнює {result}")