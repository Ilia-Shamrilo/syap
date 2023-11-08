# A=(X^T⋅X)^(-1)⋅(X^T⋅Y)
# Y = a0 + a1x1 + a2x2

import numpy as np

N = 6

x = np.column_stack((np.ones(12, dtype=int), np.arange(6, 6 + 12), np.random.randint(60, 83, 12)))
y = np.array([13.5, 13.6, 14.2, 14.8, 16.2, 16.5, 17.1, 16.8, 17.7, 18.2, 18.4, 18.6]).reshape(-1, 1)

x_trans = x.T # транспортирование х
xx = np.dot(x_trans, x) # умножение транспонированной на х
xx_inverse = np.linalg.inv(xx) # возведение в -1 степень
xy = np.dot(x_trans, y) # умножение транспонированной на y
a = np.dot(xx_inverse, xy) # рез

y_estimate = a[0] + a[1] * x[:, 1] + a[2] * x[:, 2]

print("Оценка Y:/n", y_estimate)
print(y)