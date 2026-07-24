class Solution:
    def isValid(self, s: str) -> bool:
        valid = { '(':')', '{':'}', '[':']' }

        opener = deque()

        for c in s:
            if c in valid.keys():
                opener.append(c)
            elif c in valid.values():
                if not opener: return False
                last = opener.pop()
                if c is not valid[last]:
                    return False
            
        return not opener
                
