class Solution:
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node):
        self.queueA.insert(0, node)

    def pop(self):
        if self.queueA == []:
            return None
        while len(self.queueA) != 1:
            self.queueB.insert(0, self.queueA.pop())
        self.queueA, self.queueB = self.queueB, self.queueA
        return self.queueB.pop()


if __name__ == '__main__':
    P = Solution()
    P.push(node=10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    P.push(12)
    print(P.pop())
    print(P.pop())
