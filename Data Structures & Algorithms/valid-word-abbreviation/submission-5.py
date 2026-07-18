class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while j < len(abbr):
            if i < len(word) and word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isnumeric():
                if abbr[j] == "0": return False
                k = j
                while k < len(abbr) and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False

        return i == len(word) and j == len(abbr)