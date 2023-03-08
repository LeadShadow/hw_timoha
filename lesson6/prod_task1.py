# 'Sasha' -> 5,  len('Sasha') -> 5

# Введіть знижку у % -> 20

# str = '100' -> str[0]
def apply_discount(discount: str):
    if len(discount) == 1:
        discount = '0.0' + discount[0]  # 0.0 + 9 -> '0.09'
    elif len(discount) == 2:
        discount = '0.' + discount[0] + discount[1]  # 0. + 2 + 0 -> '0.20'
    elif len(discount) == 3:
        discount = '1'
    return float(discount)


def discount_price(price, discount):
    def apply_discount_1():
        nonlocal price
        price = price * (1 - discount)

    apply_discount_1()
    return price

# 50% -> 0.5
user_input_price = int(input('Input Price: '))
user_input_discount = input('Input Discount: ')
discount = apply_discount(user_input_discount)  # 0.3
print(discount_price(user_input_price, discount))