def equation_writing(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a == 0:
        print('{} = {}'.format(b, c))
    elif a != 0 and b == 0:
        print('{} x = {}'.format(a, c))
    elif a != 0 and b > 0:
        print('{} x + {} = {}'.format(a, b, c))
    else:
        print('{} x - {} = {}'.format(a, -b, c))
