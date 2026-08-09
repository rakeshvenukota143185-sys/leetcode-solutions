class Solution:
    def wiggleSort(self, nums):
        nums.sort()

        n = len(nums)
        mid = (n + 1) // 2

        small = nums[:mid][::-1]
        large = nums[mid:][::-1]

        i = 0
        j = 0

        for k in range(n):
            if k % 2 == 0:
                nums[k] = small[i]
                i += 1
            else:
                nums[k] = large[j]
                j += 1
        
