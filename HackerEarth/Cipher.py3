#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cipher-1/

string = input()
translate = int(input())

for c in string:
  if ord(c) >= 48 and ord(c) <= 57:
    if ord(c) + (translate % 10) <=57:
      print(chr(ord(c) + translate % 10), end="")
    else:
      print(chr(((ord(c) + (translate % 10)) % 58) + 48), end="")
  elif ord(c) >= 65 and ord(c) <= 90:
    if ord(c) + translate % 26 <=90:
      print(chr(ord(c) + translate % 26), end="")
    else:
      print(chr(((ord(c) + (translate % 26)) % 91) + 65), end="")
  elif ord(c) >= 97 and ord(c) <= 122:
    if ord(c) + translate % 26 <=122:
      print(chr(ord(c) + translate % 26), end="")
    else:
      print(chr(((ord(c) + (translate % 26)) % 123) + 97), end="")
  else:
    print(c, end="")
  