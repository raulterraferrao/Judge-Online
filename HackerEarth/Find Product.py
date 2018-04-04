#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

entry = int(input())
hello = input().split()
answer = 1
for count in range(entry):
  answer = (answer * int(hello[count])) % (10**9 + 7)

print(answer)