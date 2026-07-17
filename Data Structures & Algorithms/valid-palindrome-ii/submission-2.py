class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str, skipped: bool):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r] and skipped:
                    return False
                elif s[l] != s[r] and not skipped:
                    return isPalindrome(s[l+1:r+1], True) or isPalindrome(s[l:r], True)
                l += 1
                r -= 1
            return True

        return isPalindrome(s, False)
                