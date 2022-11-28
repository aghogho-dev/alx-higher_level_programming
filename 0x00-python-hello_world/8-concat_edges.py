#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = [b for (idx, b) in enumerate([a for a in str.split(' ') if a]) if (idx in (0, 5, 6, 12))]
str = " ".join(str[1:] + [str[0]])
print(str)
