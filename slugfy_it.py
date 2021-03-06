#!/usr/bin/env python
from slugify import slugify
import sys

if __name__ == '__main__':
    arg = sys.argv[1]
    if arg.endswith('.txt'):
        with open(arg, 'r') as f:
            lines = f.read().split('\n')

        for l in lines:
            print(slugify(l))
    else:
        print(slugify(arg))

