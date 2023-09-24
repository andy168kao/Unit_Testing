def find_y(point1, point2, x):
    x1, y1 = point1
    x2, y2 = point2

    m = (y2 - y1) / (x2 - x1)

    b = y1 - m * x1

    y = m * x + b

    return y


def is_on_line(point1, point2, point3):
    x3, y3 = point3
    y_expected = find_y(point1, point2, x3)
    return y3 == y_expected
