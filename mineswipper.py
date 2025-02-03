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
z = [
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
            m[i].append(1)
            z[i].append(0)
        else:
            m[i].append(1)
            z[i].append(0)
#for i in range(10):
#    z[0].append(0)
#    z[11].append(0)
#    z[i].append(0)
#    z[i].append(0)

fig = plt.figure(figsize=(10, 6))
ax = plt.subplot(1, 2, 1)
plt.imshow(m, cmap="hot")

i = 0
while(i < 15):
    x = randint(0, 9)
    y = randint(0, 9)
    if m[x][y] == 0 or m[x][y] == 1:
        m[x][y] = -1
        z[y][x] = 10
        if(y > 0 and y < 9 and z[y-1][x] != 10):
            z[y-1][x] += 1
        if(y > 0 and y < 9 and z[y + 1][x] != 10):
            z[y+1][x] += 1
        if(y == 0 and z[y+1][x] != 10):
            z[y+1][x] += 1
        elif(y == 9 and z[y-1][x] != 10):
            z[y-1][x] += 1

        if (x > 0 and x < 9 and z[y][x-1] != 10):
            z[y][x-1] += 1
        if (x > 0 and x < 9 and z[y][x+1] != 10):
            z[y][x+1] += 1
        if (x == 0 and z[y][x+1] != 10):
            z[y][x+1] += 1
        elif (x == 9 and z[y][x-1] != 10):
            z[y][x-1] += 1

        if(x > 0 and y > 0 and z[y-1][x-1] != 10):
            z[y-1][x-1] += 1
        if(x <  9 and y < 9 and z[y+1][x+1] != 10):
            z[y+1][x+1] += 1
        if(y > 0 and x < 9 and z[y-1][x+1] != 10):
            z[y-1][x+1] += 1
        if (x > 0 and y < 9 and z[y + 1][x - 1] != 10):
            z[y + 1][x - 1] += 1
        cil = plt.Circle((x, y), 0.35, color="#c41414")
        ax.add_patch(cil)
        i += 1
for i in z:
    print(i)
plt.xticks(range(10), labels=[f"{i}" for i in range(1, 11)])
plt.yticks(range(10), labels=[f"{i}" for i in range(10, 0, -1)])
plt.xticks([i + 0.5 for i in range(10)])
plt.yticks([i + 0.5 for i in range(10)])
plt.grid(color="white")
ax = plt.subplot(1, 2, 2)

plt.imshow(z, cmap="OrRd")



for i in range(10):
    for j in range(10):
        if(z[i][j] == 10):
            plt.text(j, i, "M")
        else:
            plt.text(j, i, z[i][j])
plt.xticks(range(10), labels=[f"{i}" for i in range(1, 11)])
plt.yticks(range(10), labels=[f"{i}" for i in range(10, 0, -1)])

plt.xticks([i + 0.5 for i in range(10)])
plt.yticks([i + 0.5 for i in range(10)])

plt.grid(color="black", linestyle="--", linewidth=1.5)

plt.show()

#plt.text(j, i, "M")