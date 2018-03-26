'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''


# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()  # 按字母顺序排序
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i - 1]:
                continue  # 相等则跳过
            #print(charList[:i])
            #print(charList[i + 1:])
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))
            for j in temp:
                pStr.append(charList[i] + j)
        return pStr

    # 扩展习题, 生成字符的所有组合
    # 比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], ab和ba属于不同的排列, 但属于同一个组合
    def group(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            pStr.append(charList[i])
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            temp = self.group(''.join(charList[i + 1:]))
            for j in temp:
                pStr.append(charList[i] + j)
            pStr = list(set(pStr))
            pStr.sort()
        return pStr


ss = 'acbea'
S = Solution()
print(S.Permutation(ss),len(S.Permutation(ss)))
print()
#print(S.group(ss))
