'''Реализуйте функцию get_discount_price_customer для расчета цены на товар
интернет-магазина с учетом скидки клиента.

Функция принимает два параметра:

price — цена продукта
customer — словарь с данными клиента следующего вида: {"name": "Dima"} или
{"name": "Boris", "discount": 0.15}
У вас есть глобальная переменная DEFAULT_DISCOUNT, которая определяет скидку для клиента,
если у него нет поля discount.

Функция get_discount_price_customer должна возвращать новую цену на товар для клиента.

Напомним, что дисконт discount — это дробное число от 0 до 1. И мы под скидкой понимаем коэффициент,
который определяет размер от цены. И на этот размер мы понижаем итоговую цену товара:
price = price * (1 - discount).
'''

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    def new_discount():
        if 'discount' not in customer:
            customer['discount'] = DEFAULT_DISCOUNT
        return (1 - customer['discount']) * price
    return new_discount()


if __name__ == "__main__":
    print(get_discount_price_customer(1000, {"name": "Boris"}))