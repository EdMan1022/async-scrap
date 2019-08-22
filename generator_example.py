from itertools import cycle


def endless():
    yield from cycle((9, 8, 7, 6))


e = endless()
total = 0
for i in e:
    if total < 30:
        print(i, end=" ")
        total += i
    else:
        print()
        break

print((next(e), next(e), next(e)))
