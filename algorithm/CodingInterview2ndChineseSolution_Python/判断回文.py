def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


def isPalindrome1(s):
    for i in range(len(s)//2) :
        if not s[i] == s[len(s) - i - 1]:
            return False
    return True


def isPalindrome2(s):
    return s == s[::-1]



s="cabac"
print(isPalindrome1(s))
