# and (І) -> множення(вираз виконається якщо обидві умови виконаються)
# a       b      a and b
# True   True     True
# True   False    False
# False  True     False
# False  False    False

# True -> 1
# False -> 0
# 1 * 1 -> 1
# 1 * 0 -> 0
# 0 * 1 -> 0
# 0 * 0 -> 0
a = True and False  # False

# or (АБО) -> додавання(вираз виконається, якщо хоча б одна з умов виконується)
# a       b     a or b
# True   True    True
# True   False   True
# False  True    True
# False  False   False

a = True or False  # True

# not (НЕ) -> заперечення, вираз виконається якщо операнд брехня
# a      not a
# True   False
# False  True