from decimal import Decimal, getcontext
print(0.1 + 0.2 == 0.3)

# 111 -> 7
print(round(1 / 7, 2))

getcontext().prec = 6
print(Decimal(1) / Decimal(7))
print(Decimal(2) / Decimal(7))
