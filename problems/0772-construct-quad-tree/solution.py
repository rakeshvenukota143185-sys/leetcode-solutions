class Solution:
    def construct(self, grid):
        
        def build(r, c, size):
            value = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != value:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(value == 1, True)

            half = size // 2

            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)

            root = Node(True, False)
            root.topLeft = topLeft
            root.topRight = topRight
            root.bottomLeft = bottomLeft
            root.bottomRight = bottomRight

            return root

        return build(0, 0, len(grid))
