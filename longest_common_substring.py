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
# def LongestCommonSubstring(i,j,length):
#         if i==0 or j==0:
#             return length
#         elif s1[i-1]==s2[j-1]:
#             length = LongestCommonSubstring(i-1,j-1, length+1)
#         length = max(length, max(LongestCommonSubstring(i-1,j,0), LongestCommonSubstring(i,j-1,0)))
#         return length
def LongestCommonSubstringDP(s1,s2,m,n):
    dp = [[0 for col in range(n+1)] for row in range(m+1)]
    length = 0
    for row in range(m+1):
        for col in range(n+1):
            if row==0 or col==0:
                dp[row][col] = 0
            elif s1[row-1] == s2[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
                length = max(length, dp[row][col])
            else:
                dp[row][col] = 0
    return length

for _ in range(int(input())):
    m,n = map(int,input().split())
    s1 = input()
    s2 = input()
    print(LongestCommonSubstringDP(s1,s2,m,n))
    #dp = [[0 for x in range(len(s1))] for y in range(len(s2))]
    

