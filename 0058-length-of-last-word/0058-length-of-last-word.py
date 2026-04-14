class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordcount = 0
        n = len(s) - 1
        for i in range(n, -1, -1):
            if s[i] == " " and wordcount == 0:
                continue
            elif s[i] == " ":
                break
            else:
                wordcount += 1    
        return wordcount