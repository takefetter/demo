import unittest


class Solution:
    def PowerWithUnsignedExponent(self, base, exponent):
        if (exponent == 0):
            return 1
        if (exponent == 1):
            return base

        result = self.PowerWithUnsignedExponent(base, exponent >> 1)
        result *= result
        if ((exponent & 0x1) == 1 and exponent > 0):
            result *= base
        return result


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_1(self):
        base = 1
        exponent = 100
        self.assertEqual(self.s.PowerWithUnsignedExponent(base, exponent), 1)

    # def test_2(self):
    #     base = -1
    #     exponent = -1
    #     self.assertEqual(self.s.PowerWithUnsignedExponent(base, exponent), 1)

    def test_3(self):
        base = 0
        exponent = 0
        self.assertEqual(self.s.PowerWithUnsignedExponent(base, exponent), 1)
        base = -1
        exponent = 1
        self.assertEqual(self.s.PowerWithUnsignedExponent(base, exponent), -1)

    if __name__ == '__main__':
        unittest.main()
