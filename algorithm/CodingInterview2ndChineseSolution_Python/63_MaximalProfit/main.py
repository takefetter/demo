class Solution:
    def MaxDiff(self, numbers, length):
        if numbers == None and length < 2:
            return 0
        min = numbers[0]
        maxDiff = numbers[1] - min

        for i in range(2, length):
            if numbers[i - 1] < min:
                min = numbers[i - 1]

            currrentDiff = numbers[i] - min
            if currrentDiff > maxDiff:
                maxDiff = currrentDiff

        return maxDiff
