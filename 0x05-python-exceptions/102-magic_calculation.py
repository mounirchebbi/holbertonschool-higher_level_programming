#!/usr/bin/python3
def magic_calculation(a, b):
    out = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                out += a ** b / i
        except:
            out = b + a
            break
    return (out)
