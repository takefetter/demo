# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == None or len(s) <= 0:
            return -1
        alphabet = {}

        alist = list(s)
        for i in alist:
            if i not in alphabet.keys():
                alphabet[i] = 0
            alphabet[i] += 1
        for i in alist:
            if alphabet[i] == 1:
                return i
        return -1


s = Solution()
print(s.FirstNotRepeatingChar('google'))
