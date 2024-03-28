#!/usr/bin/python3
import functools
print(functools.reduce(lambda x, y: x + y, map(chr, range(65, 91))))
