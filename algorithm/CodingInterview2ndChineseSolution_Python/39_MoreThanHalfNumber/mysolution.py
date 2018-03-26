class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers: return 0
        res = 0
        times = 0
        for i, num in enumerate(numbers):
            if times == 0:
                res = num
                times = 1
            elif num == res:
                times += 1
            else:
                times -= 1
        return res if numbers.count(res) > len(numbers) / 2 else 0
