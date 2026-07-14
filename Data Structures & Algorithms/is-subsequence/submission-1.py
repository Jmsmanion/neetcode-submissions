class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s is "": return True
        ls = lt = 0

        while lt < len(t):
            if s[ls] is t[lt]:
                ls += 1 
                lt += 1
            else:
                lt += 1

            if not ls < len(s):
                return True
            
        return False