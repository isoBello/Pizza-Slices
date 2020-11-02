# -*- coding: utf-8 -*-
def kadane(n, a):
    mmax = 0
    mend = 0
    for i in range(0, n):
        mend = mend + a[i]
        if mend < 0:
            mend = 0
        if mmax < mend:
            mmax = mend
    return mmax


def max_sum(n, a):
    kad = kadane(n, a)
    mcorner = 0
    for i in range(0, n):
        mcorner += a[i]
        a[i] = -a[i]
    mcorner = mcorner + kadane(n, a)
    if mcorner > kad:
        return mcorner
    else:
        return kad


if __name__ == "__main__":
    fatias = int(input())
    array = list(map(int, input().split(" ")))
    ans = max_sum(fatias, array)
    if ans < 0:
        print(0)
    else:
        print(ans)
