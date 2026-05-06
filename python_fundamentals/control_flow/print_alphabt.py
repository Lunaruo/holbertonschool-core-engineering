#!/usr/bin/env python3

s = ""
for c in range(ord('a'), ord('z') + 1):
    if c != ord('e') and c != ord('q'):
        s += chr(c)

print("{}".format(s))
