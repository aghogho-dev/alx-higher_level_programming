#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{a} + {b} = {c}".format(b = b, a = a, c = add(a, b)))
    print("{a} - {b} = {c}".format(a=a, b=b, c=sub(a, b)))
    print("{a} * {b} = {c}".format(a=a, b=b, c=mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
