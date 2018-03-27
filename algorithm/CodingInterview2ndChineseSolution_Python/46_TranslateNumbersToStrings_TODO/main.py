class Solution:
    ord('a') - 97

    def GetTranlsationCount(self, number):
        if number < 0:
            return 0
        numberInstring = number.__str__()
        return self.GetTranslationCount1(numberInstring)

    def GetTranslationCount1(self, number):
        length = len(number)
        counts = [0] * length
        print(counts)
        for i in range(length):
            count = 0
            if (i < length - 1):
                count = counts[i + 1]
            else:
                count = 1

            if i < length - 1:
                digit1 = int(number[i])
                digit2 = int(number[i + 1])
                converted = digit1 * 10 + digit2
                if converted > 10 and converted <= 25:
                    if i < length - 2:
                        count += counts[i + 2]
                    else:
                        count += 1
            counts[i] = count
        return counts[0]


s = Solution()
print(s.GetTranlsationCount(12258))
