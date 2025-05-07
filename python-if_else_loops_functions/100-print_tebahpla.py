#!/usr/bin/python3

print("".join(
    "{}".format(chr(i).upper()) if (i - 122) % 2 != 0 else "{}".format(chr(i))
    for i in range(122, 96, -1)
), end="")
