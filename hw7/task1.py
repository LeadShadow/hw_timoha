# Одна из классических задач на понимание рекурсии, которую часто задают на собеседованиях,
# особенно начинающим программистам — это ряд Фибоначчи.
#
# Ряд Фибоначчи — это последовательность чисел вида: 0, 1, 1, 2, 3, 5, 8, ... где каждое следующее
# число последовательности получается сложением двух предыдущих членов ряда.
#
# В общем виде для вычисления n-го члена ряда Фибоначчи нужно вычислить выражение: Fn = Fn-1 + Fn-2.
#
# Эту задачу можно решить рекурсивно, вызывая функцию, вычисляющую числа последовательности до тех
# пор, пока вызов не дойдет до членов ряда меньше n = 1, где последовательность задана.
def fibonacci(n):