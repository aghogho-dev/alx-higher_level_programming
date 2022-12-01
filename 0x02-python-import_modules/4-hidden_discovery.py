#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    hiddens = [v for v in dir(hidden_4) if not v.startswith('__')]
    for value in hiddens:
        print("{}".format(value))
