'''
Constraints
  O: list of paren strs
  I: int N, 1 <= N <= 8

Ideas
  1. 
  - N individual parens '()()()'
  - N - 1 individual parens inside 1
    '(()())'
  - N nested parens
  * always start with (
  * always end with )
  (
  /     \
 ()      ((
 /       /  \
()(      (()) ((()))
 /.   \       \   
()()() ()(()). (())()
N = 3

Test Cases
  1. N = 1 --> ['()']
  2. N = 2 --> ['()()', '(())']
  3. N = 3 --> 
  ["((()))","(()())","(())()","()(())","()()()"]
'''