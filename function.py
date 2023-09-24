def find_y(point1, point2, x):
    x1, y1 = point1
    x2, y2 = point2

    m = (y2 - y1) / (x2 - x1)

    b = y1 - m * x1

    y = m * x + b

    return y
