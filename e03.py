# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

while True:
    coord_read = input('Введите кординаты точек на прямой {x1, y1} {x2, y2}: ').split()
    if len(coord_read) == 4 and \
            not sum([not d.isdecimal() for d in coord_read]) and \
            not (coord_read[0] == coord_read[2] and coord_read[1] == coord_read[3]):
        break
    print("Неверно введены данные!")

x1, y1, x2, y2 = [float(x) for x in coord_read]
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')
