def by_x(year, div, ret):
    return 0 if year % div else ret


def get_year(y):
    return by_x(y, 4, 1) + by_x(y, 100, 2) + by_x(y, 400, 4)


def is_leap_year(x):
    n = get_year(x)
    if n in [1, 5, 7]:
        return True
    else:
        return False
