# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
from random import randint
import matplotlib.pyplot as plt

m =  [0, 0, 0, 0, 0, 0]
r1 = randint(0, 5)
mx = 0
cnt = 1
m[r1] += 1
print(r1)
for i in range(999):
    r2 = randint(0, 5)
    print(r2)
    m[r2] += 1
    if(r1 == r2):
        cnt += 1
    else:
        mx = max(mx, cnt)
        cnt = 1
    r1 = r2
mx = max(mx, cnt)
for i in range(1, 7):
    print("Вероятность выпадения числа ", i, ": ", m[i-1]/10, "%", sep='')
print()
print("Максимальное количество подряд выпавших одинаковых значений:", mx)
categories = [1, 2, 3, 4, 5, 6]
values = [m[0], m[1], m[2], m[3], m[4], m[5]]
plt.bar(categories, values, color='#5da38f')
plt.show()