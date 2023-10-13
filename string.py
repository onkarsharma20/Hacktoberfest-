# code to count all possible substrings that have exactly k distinct character

def solve(s,k):
    count = 0
    ans = ''
    d = dict()
    start = 0
    for i in range(len(s)):
        ans+=s[i]
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]] = 1
        while len(d)>k:
            d[s[start]]-=1
            if d[s[start]]==0:
                del d[s[start]]
            start+=1
            ans = ans[1:]
        count+=(i-start+1)
    return count
class Solution:
    def substrCount (self,s, k):
        return solve(s, k)-solve(s, k-1)
