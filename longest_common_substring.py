'''
Author: Satish Patel
Email: ssj.satish@gmail.com
2
6 6
ABCDGH
ACDGHR
3 2
ABC
AC

Solution:

The longest common suffix has following optimal substructure property.

If last characters match, then we reduce both lengths by 1
LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
If last characters do not match, then result is 0, i.e.,
LCSuff(X, Y, m, n) = 0 if (X[m-1] != Y[n-1])
Now we consider suffixes of different substrings ending at different indexes.
The maximum length Longest Common Suffix is the longest common substring.
LCSubStr(X, Y, m, n) = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m and 1 <= j <= n
'''
def longest_common_substring(s1,s2,m,n):
        if m==0 or n==0:
            return 0
        elif s1[m-1]==s2[n-1]:
            length = longest_common_substring(s1,s2,m-1,n-1) + 1
        else:
            return max(length, longest_common_substring(s1,s2,m-1,n-1))
for _ in range(int(input())):
    n,m = map(int,input().split())
    s1 = input()
    s2 = input()
    dp = [[0 for x in range(len(s1))] for y in range(len(s2))]
    

