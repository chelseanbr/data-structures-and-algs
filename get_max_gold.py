class Solution:
    def __init__(self):
        self.max_gold = 0
        self.cur_gold = 0
    
    def getMaximumGold(self, grid) -> int:
      def dfs(x, y):
          if not(0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] > 0):
              return
          temp_gold = grid[x][y]
          self.cur_gold += temp_gold
          self.max_gold = max(self.max_gold, self.cur_gold)
          grid[x][y] = 0
          for i, j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
              dfs(i, j)
          self.cur_gold -= temp_gold  
          grid[x][y] = temp_gold

      for i in range(len(grid)):
          for j in range(len(grid[0])):
              dfs(i, j)

      return self.max_gold

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
soln = Solution()
print(soln.getMaximumGold(grid))