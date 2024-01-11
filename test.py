def hi(x: str = "a"or"b"):
    if x == 'a':
        f = 'a'
    if x == 'b':
        f = 'b'
    return f
hi(x='c')