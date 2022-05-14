bracket_str = "(())()()(((()()((((()(()))))(()))))"

stack = []

for c in bracket_str:
  if c == "(":
    stack.append("(")
  elif c == ")":
    if len(stack) < 1:
      print("Stack closes too much")
      exit()
    stack.pop()
if len(stack) == 0:
  print("good stack")
else:
  print("stack doesn't close")
exit

