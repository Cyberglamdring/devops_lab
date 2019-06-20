#!/usr/bin/env python
def paintd():
    N, M = map(int,input('Input values separated by a space (e.g.: 11 33): ').split())
    a = [('.|.'*i).center(M,'-') for i in range(1,N,2)]
    for e in a+['WELCOME'.center(M,'-')]+list(reversed(a)):print(e)
    return e
print (paintd())