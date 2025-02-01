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
        mxcnt2 = max(mxcnt2, cnt2)
        cnt2 = 0
cr = sum(m) / len(m)
print(cr, cnt1, mxcnt2)

fig = plt.figure(figsize=(12, 7))
ax = plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.xlabel("День")
plt.ylabel("Температура")

ax = plt.subplot(2, 1, 2)

plt.bar(x, y, color='#5da38f')

plt.show()


