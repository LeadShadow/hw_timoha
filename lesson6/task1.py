# Необходимо реализовать функцию расчета цены на товар со скидкой discount_price. Функция
# принимает цену price и скидку discount — это дробное число от 0 до 1. Здесь, и в дальнейшем,
# мы под скидкой будем понимать коэффициент, который определяет размер от цены. И на этот размер
# мы понижаем итоговую цена товара. Логику функции необходимо прописать во внутренней функции
# apply_discount, используя объявление переменой price как nonlocal

# 100% -> 1, 30% -> 0.3

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)

    apply_discount()
    return price


print(int(discount_price(1000, 0.3)) - 1)