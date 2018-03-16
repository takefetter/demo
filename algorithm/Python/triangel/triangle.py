import math
import sys


def shape(a):
    if a[0] == a[1] and a[1] == a[2]:
        print("Equilateral\n")
    elif a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
        print("Isoceles\n")
    elif math.fabs(a[0] * a[0] + a[1] * a[1] - a[2] * a[2]) < 1e-6 or math.fabs(
            a[0] * a[0] + a[2] * a[2] - a[1] * a[1]) < 1e-6 or math.fabs(
        a[2] * a[2] + a[1] * a[1] - a[0] * a[0]) < 1e-6:
        print("Right-angled\n")
    else:
        print("General\n")


if __name__ == '__main__':

    for line in sys.stdin:
        a = line.split(' ')
        a[0] = int(a[0])
        a[1] = int(a[1])
        a[2] = int(a[2])
        if ((a[0] + a[1] > a[2]) and (a[1] + a[2] > a[0]) and (a[2] + a[0] > a[1])):  # 同时满足
            shape(a)
        else:
            print("Unable\n")
