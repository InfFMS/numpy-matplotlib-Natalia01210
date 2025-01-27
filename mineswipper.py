# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#

from random import randint
import matplotlib.pyplot as plt

m = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
for i in range(10):
    for j in range(10):
        if(i % 2 == 1 and j % 2 == 1) or (i % 2 == 0 and j % 2 == 0):
            m[i].append(0)
        else:
            m[i].append(0.00001)

fig = plt.figure(figsize=(10, 6))
ax = plt.subplot(1, 2, 1)
plt.imshow(m, cmap="magma")

i = 0
while(i < 15):
    x = randint(0, 9)
    y = randint(0, 9)
    if m[x][y] == 0 or m[x][y] == 0.00001:
        m[x][y] = -1
        cil = plt.Circle((x, y), 0.35, color="#5d66a3")
        ax.add_patch(cil)
        i += 1


plt.show()