"""
Онлайн-магазин "У Бобра" надає послугу експрес доставлення 
своїх товарів за ціною 5¤ за перший товар у замовленні та 2¤ - за всі наступні товари. 
Необхідно реалізувати функцію, яка приймає як перший параметр кількість товарів у замовленні quantity, 
але також має бути присутнім параметр, що передається тільки за ключем discount.

Параметр discount за замовчуванням має значення 0 - знижки немає. 
Приймає значення від 0 до 1. 
Функція cost_delivery повертає загальну суму за доставлення товару з урахуванням знижки.

Треба передбачити, що функція cost_delivery при визові може приймати будь-яку кількість позиційних аргументів.

Приклад:

cost_delivery(2, 1, 2, 3)
При такому виклику quantity дорівнює 2, а параметр discount за умовчанням має значення 0.

Тестові виклики функції для правильності роботи будуть наступними:

cost_delivery(2, 1, 2, 3) == 7
cost_delivery(3, 3) == 9
cost_delivery(1) == 5
cost_delivery(2, 1, 2, 3, discount=0.5) == 3.5
"""


def cost_delivery(quantity, *args, discount=0):
    first_item = 5
    next_item =2
    delivery_price = first_item + next_item * (quantity -1)
    if discount != 0:
        delivery_price = delivery_price - delivery_price * discount
    return delivery_price

assert cost_delivery(2, 1, 2, 3) == 7
assert cost_delivery(3, 3) == 9
assert cost_delivery(1) == 5
assert cost_delivery(2, 1, 2, 3, discount=0.5) == 3.5

print("All OK")