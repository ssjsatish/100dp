'''
Author: Satish Patel
Email: ssj.satish@gmail.com
'''
import sys
def min_coins(V, c, n):
    if v == 0:
        return 0
    result = sys.maxsize
    for i in range(n):
        temp = min_coins(V-c[i], c, n)
for _ in range(int(input())):
    v,n = map(int, input().split())
    c = [int(x) for x in input().split()]
