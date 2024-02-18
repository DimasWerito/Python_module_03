"""
Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. 
Ми маємо 7 призів для розіграшу. 
Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? 
Для цього ми будемо використовувати формулу сполучень без повторень

Cnk = n! / ((n - k)! · k!)

де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

Напишіть функцію number_of_groups, яка приймає параметри n та k, 
і за допомогою функції factorial повертає нам скільки різних списків переможців ми можемо отримати при розіграші

Зверніть увагу на те, які великі значення ми отримуємо для факторіала. 
Рекурсивні висловлювання треба завжди застосовувати з обережністю при обчисленнях, щоб не отримати переповнення пам'яті.
"""


def factorial(n):
    print(f"Current n {n}")
    if n < 2:
        print(f"Base {n}")
        return 1  # Базовий випадок
    else:
        result = n * factorial(n - 1)  # Рекурсивний випадок
        print(f"Recursion {result}")
        return result
    
        
    
        


def number_of_groups(n, k):
    # Cnk = n! / ((n - k)! · k!)
    result = factorial(n) / (factorial(n - k) * factorial(k))
    return int(result)