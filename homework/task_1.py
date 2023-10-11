def check_range(x, y, z):
    if y <= x <= z:
        return 'x jest między y a z'
    else:
        return 'x NIE jest między y a z'


def bool_range(x, y, z):
    return y <= x <= z
