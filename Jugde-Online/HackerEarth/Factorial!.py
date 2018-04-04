#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

entry = int(input())
answer = 1
for i in range(entry):
  answer = answer * (i + 1)

print(answer)