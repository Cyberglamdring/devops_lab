#!/usr/bin/env python
firstinput = int(input('Input int M = ',))
setone = set(map(int,input('Input contains M space-separeted int: ',).split()))

secondinput = int(input('Input int N = ',))
settwo = set(map(int,input('Input contains N space-separeted int: ',).split()))

settree = (setone.difference(settwo)).union(settwo.difference(setone))

print ("Summetric difference:")
for i in sorted(list(settree)):print (i)