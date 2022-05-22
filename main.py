import numpy as np
from numpy import random
import matplotlib.pyplot as plt

num = 10000000 # 試行回数

x = [random.uniform(0, 1) for i in range(num)]
y = [random.uniform(0, 1) for i in range(num)]
#点を生成
# √x^2 + y^2が原点からの距離それが1より上かしたかで判断
points = np.hypot(x, y)
count = 0
for i in points:
    if i <= 1:
        count += 1

pi = (count / num) * 4.0
print(f"{pi}")
plt.plot(x, y, '.')

# x^2 + y^2 = 1の式を使って円の第1象限を記述
x_pi = [i for i in np.arange(0.0, 1.01, 0.01)]
y_pi = np.sqrt(1 - np.square(x_pi))  # y = √1-x^2

plt.plot(x_pi, y_pi)
plt.xlim(0., 1.)
plt.ylim(0., 1.)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo")

plt.show()