string = input()
flag = False
for c in string:
  if c != 'G' and c != 'C' and c != 'T' and c != 'A':
    print('Invalid Input')
    flag = True
    break
if flag != True:
  for c in string:
    if c == 'G':
      print('C',end="")
    elif c == 'C':
      print('G',end="")
    elif c == 'T':
      print('A',end="")
    elif c == 'A':
      print('U',end="")
