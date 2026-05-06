#!/usr/bin/env python3

print("{}".format(''.join(
    chr(c) for c in range(ord('a'), ord('z') + 1)
    if c != ord('e') and c != ord('q')
)))
