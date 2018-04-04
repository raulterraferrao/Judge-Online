#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/

entry = int(input())
for i in range(entry):
  seat = int(input()) - 1
  if (seat // 6) % 2 == 0:
    if seat % 6 == 0:
      result = str(seat + 12) + " WS"
    elif seat % 6 == 1:
      result = str(seat + 10) + " MS"
    elif seat % 6 == 2:
      result = str(seat + 8) + " AS"
    elif seat % 6 == 3:
      result = str(seat + 6) + " AS"
    elif seat % 6 == 4:
      result = str(seat + 4) + " MS"
    elif seat % 6 == 5:
      result = str(seat + 2) + " WS"
  if (seat // 6) % 2 == 1:
    if seat % 6 == 0:
      result = str(seat - 0) + " WS"
    elif seat % 6 == 1:
      result = str(seat - 2) + " MS"
    elif seat % 6 == 2:
      result = str(seat - 4) + " AS"
    elif seat % 6 == 3:
      result = str(seat - 6) + " AS"
    elif seat % 6 == 4:
      result = str(seat - 8) + " MS"
    elif seat % 6 == 5:
      result = str(seat - 10) + " WS"
  print(result)
