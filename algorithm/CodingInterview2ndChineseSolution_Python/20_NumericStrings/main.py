# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
