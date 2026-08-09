class Solution:
    def kthLargestValue(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])

        values = []
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    matrix[i - 1][j - 1]
                    ^ prefix[i - 1][j]
                    ^ prefix[i][j - 1]
                    ^ prefix[i - 1][j - 1]
                )

                values.append(prefix[i][j])

        values.sort(reverse=True)

        return values[k - 1]
        
