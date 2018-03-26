# coding=utf-8

# 风格1
def queen(A, cur=0):
    if cur == len(A):
        print(A)
    else:
        for col in range(len(A)):
            A[cur] = col  # 表示把第cur行的皇后放在col列上
            ok = True
            for r in range(cur):
                if A[r] == col or r - A[r] == cur - A[cur] or r + A[r] == cur + A[cur]:  # 判断是否跟前面的皇后冲突
                    ok = False
                    break
            if ok:
                queen(A, cur + 1)

            # 风格2


def queen(A, cur=0):
    if cur == len(A):
        print(A)
    else:
        for col in range(len(A)):
            A[cur] = col  # 表示把第cur行的皇后放在col列上
            for r in range(cur):
                if A[r] == col or r - A[r] == cur - A[cur] or r + A[r] == cur + A[cur]:  # 判断是否跟前面的皇后冲突
                    break
            else:
                queen(A, cur + 1)

            # 风格3


def queen(A, cur=0):
    if cur == len(A):
        print(A)
        printqueen(A)
    else:
        for col in range(len(A)):
            A[cur] = col  # 表示把第cur行的皇后放在col列上
            if all(A[r] != A[cur] and r - A[r] != cur - A[cur] and r + A[r] != cur + A[cur] for r in
                   range(cur)):  # 判断是否跟前面的皇后冲突
                queen(A, cur + 1)


def printqueen(A):
    queenpos = []
    for i in range(len(A)):
        queenpos.append([i, A[i]])
    for k in range(len(A)):
        for j in range(len(A)):
            if [k, j] in queenpos:
                print('*', end='   ')
            else:
                print('-', end='   ')
        print("\n")


queen([None] * 8)
