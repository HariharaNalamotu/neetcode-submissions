class Solution:
    grid = []

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        numislands = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "1":
                    self.recursiveRemove(i, j)
                    numislands += 1

        return numislands

    def recursiveRemove(self, i, j):
        if self.grid[i][j] == "1":
            self.grid[i][j] = "0"
            if j < len(self.grid[i]) - 1:
                self.recursiveRemove(i, j + 1)
            if j > 0:
                self.recursiveRemove(i, j - 1)
            if i < len(self.grid) - 1:
                self.recursiveRemove(i + 1, j)
            if i > 0:
                self.recursiveRemove(i - 1, j)
