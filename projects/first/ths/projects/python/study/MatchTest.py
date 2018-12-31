# -*- coding: utf-8 -*-
import math


def quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))

# 使用3层for循环打印对称式，对称数比如：‘121’
print([100 * i + 10 * j + k for i in range(1, 10) for j in range(0, 10) for k in range(1, 10) if k == i])
