# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
from random import randint

import matplotlib.pyplot as plt
import numpy as np
m = []
cnt1 = 0
cnt2 = 0
mxcnt2 = 0
r = 0
x = []
y = []
for i in range(365):
    now = randint(-10, 40)
    x.append(i+1)
    y.append(now)
    m.append(now)
    if(now > 25):
        cnt1 += 1
    if(now < 0):
        cnt2 += 1
    else:
        if(cnt2 > mxcnt2):
            r = i+1
            mxcnt2 = cnt2
        cnt2 = 0
cr = sum(m) / len(m)
print("Средняя температура за год:", cr)
print("Количество дней с температурой выше 25:", cnt1)
print("Самая длинная последовательность дней, когда температура была ниже 0:")
print(chr(9), "Длина этой последовательности:", mxcnt2)
print(chr(9), "Номера крайних дней:", r - mxcnt2 + 1, r)

fig = plt.figure(figsize=(12, 7))
ax = plt.subplot(3, 1, 1)
plt.plot(x, y)

ax = plt.subplot(3, 1, 2)

plt.bar(x, y, color='#5da38f')

ax = plt.subplot(3, 1, 3)

cmap = plt.get_cmap('viridis')
norm = plt.Normalize(-10, 35)
line_colors = cmap(norm(y))
plt.scatter(x, y, color=line_colors)


plt.show()


