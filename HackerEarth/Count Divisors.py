#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

l,r,k = map(int,input().split())
answer = 0
for count in range(l,r + 1):
  if count % k == 0: answer += 1

print(answer)