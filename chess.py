# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
from random import randint

import matplotlib.pyplot as plt
import numpy as np

data = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]
fig, ax = plt.subplots()
plt.imshow(data, cmap='hot')

a = randint(0, 7)
b = randint(0, 7)



for x in range(8):
    k = (x, b)
    cil = plt.Circle(k, 0.35, color="#5d66a3")
    ax.add_patch(cil)
for x in range(8):
    k = (a, x)
    cil = plt.Circle(k, 0.35, color='#5d66a3')
    ax.add_patch(cil)
for x in range(8):
    if(a + b - x >= 0):
        k = (a + b - x, x)
        cil = plt.Circle(k, 0.35, color='#5d66a3')
        ax.add_patch(cil)
for x in range(8):
     if(x + (a - b) < 8):
        k = (x + (a - b), x)
        cil = plt.Circle(k, 0.35, color='#5d66a3')
        ax.add_patch(cil)
cil = plt.Circle((a, b), 0.42, color='#2c3047')
ax.add_patch(cil)
plt.xticks(range(8), labels=[f"{chr(i)}" for i in range(65, 65+8)])
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
plt.show()