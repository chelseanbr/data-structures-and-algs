'''
Constraints
  O: array of split pal strs
  I: str s
Ideas
  1. left pal, right pal
    s = "abcba"
        /          \     \      \        \
  a,bcba           ab,cba abc,ba abcb,a  abcba v
   /   \        \      x     x       x
a,b,cba a,bc,ba a,bcb,a
left has to be pal, recurse on right
pal: single char or check w/ 2 ptrs
Test Cases
          |.   |
          01234
  1. s = "abcba" len(s) = 5
  2. ''
  3. 'abc'      
  
  result = []
    split_pal_strs = ['a']
    l = 0
    a
    ^
'''
def partition(s):
    def is_pal(l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def dfs(start_ind, path):
        if start_ind >= len(s): res.append(path)
            
        for l in range(len(s) - start_ind):
            if is_pal(start_ind, start_ind + l):
                dfs(start_ind + l + 1, path + [s[start_ind:start_ind + l + 1]] )
    
    res = []
    dfs(0,[])
    return res
print(partition('abcba'))