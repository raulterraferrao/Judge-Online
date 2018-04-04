#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

string = input()
if(string[::-1] == string):
  print("YES")
else:
  print('NO')
