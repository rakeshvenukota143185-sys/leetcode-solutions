class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i in range(self.n):
            self.add(i + 1, nums[i])

    def add(self, index, value):
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

    def prefixSum(self, index):
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total

    def update(self, index, val):
        difference = val - self.nums[index]

        self.nums[index] = val

        self.add(index + 1, difference)

    def sumRange(self, left, right):
        return self.prefixSum(right + 1) - self.prefixSum(left)
