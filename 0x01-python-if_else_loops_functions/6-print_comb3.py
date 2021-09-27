#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a, 10):
        if a == b:
            continue
        if a == 10 & b == 8:
            break
        print("{}{}".format(a, b), end=", ")
print(89)
