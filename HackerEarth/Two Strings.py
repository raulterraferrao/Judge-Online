#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/

entry = int(input())
for i in range(entry):
  string1, string2 = input().split()
  for c in string1:
    if c in string2:
      string1 = string1.replace(c, '', 1)
      string2 = string2.replace(c, '', 1)
  if len(string1) + len(string2) > 1:
    print('NO')
  else:
    print('YES')