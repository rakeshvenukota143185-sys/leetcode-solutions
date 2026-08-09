class Solution:
    def longestSubstring(self, s, k):
        def solve(left, right):
            if right - left < k:
                return 0

            count = [0] * 26

            for i in range(left, right):
                count[ord(s[i]) - ord('a')] += 1

            for i in range(left, right):
                if count[ord(s[i]) - ord('a')] < k:
                    j = i + 1

                    while j < right and count[ord(s[j]) - ord('a')] < k:
                        j += 1

                    return max(
                        solve(left, i),
                        solve(j, right)
                    )

            return right - left

        return solve(0, len(s))
        
