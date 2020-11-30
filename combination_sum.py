'''
Constraints
  O: list of combinations of nums that sum to target
  I: list of unique pos nums, int target
    * 1 <= target <= 500
    * 1 <= candidates.length <= 30
Ideas
  1. BRUTE FORCE:
    Try all combinations = O(n^n)
  2. 
  - Sort array, O(n log n) time


Test Cases
  1. numbers = [2,4,6,3], target = 6

  self.combos = []
  cur_combo = [2]
  combination_sum_helper(candidates, target - cur_num, cur_combo)
  sort -> [2,3,4,6]
           ^i 
           /\
      [2,4] [2,2,2]         
                
            3
            /\
          2,1 3

  1. init self.combos = []
  2. scan through nums, for each num <= target, init empty array
  3. if cur num == target, append array
    elif cur num < target, new target is diff, recurse
    if cur num > target, return None



'''
class Combination_Sum:
  def __init__(self):
    self.combos = []
  
  def combination_sum(self, candidates, target):
    def combination_sum_helper(candidates, target, idx, cur_combo):
      if target == 0:
        self.combos.append(cur_combo)
      if target <= 0 or idx >= len(candidates):
        return
      for i in range(idx, len(candidates)):
        if candidates[i] > target:
          break
        combination_sum_helper(candidates, target-candidates[i], i, cur_combo+[candidates[i]])

    candidates.sort()
    combination_sum_helper(candidates, target, 0, [])
    return self.combos

combo_sum = Combination_Sum()
candidates = [2,4,6,3]
target = 6
print(combo_sum.combination_sum(candidates, target))