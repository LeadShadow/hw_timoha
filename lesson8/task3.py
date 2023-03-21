# Для функции из предыдущей задачи создайте строки документации. Можно использовать
# следующий шаблон
#
#     """Функция возвращает общую сумму доставки.
#
#     Первый параметр &mdash; количество товаров в заказе.
#     Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""

def cost_delivery(quantity, *_, discount=0):
    """Функция возвращает общую сумму доставки.
    Первый параметр &mdash; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""


    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result

s = """Функция возвращает общую сумму доставки.
Первый параметр &mdash; количество товаров в заказе.
Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0
"""

print(s)

s = 'Функция возвращает общую сумму доставки.\nПервый параметр &mdash; количество товаров в заказе.\nПараметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0'
print(s)