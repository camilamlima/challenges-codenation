import math

def calc_angle_mbc(a, b):

    h = math.hypot(a, b)
    m = h / 2
    cos_b = math.acos(
        (b ** 2) / (2 * b * m)
    )

    graus = math.degrees(cos_b)
    return int(round(graus))
