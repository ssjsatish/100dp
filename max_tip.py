'''
Auhtor: Satish Patel
Email: ssj.satish@gmail.com
2
5 3 3
1 2 3 4 5
5 4 3 2 1
8 4 4
1 4 3 2 7 5 9 6 
1 2 3 6 5 4 9 8
'''
for _ in range(int(input())):
    n,x,y = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    diff = []
    for a,b in zip(A,B):
        diff.append(abs(a-b))
    diff.sort(reverse=True)
    print(diff)


