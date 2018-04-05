#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/play-with-numbers-2/

n, q  = map(int,input().split())
array = list(map(int,input().split()))
soma = [0 for i in range(n)]
soma[0] = 0
somaVar = 0
for i in range(len(array)):
  somaVar += array[i]
  soma[i] = somaVar
for _ in range(q):
  l,r = map(int,input().split())
  if(l==1):
    floor = soma[r-1]//(r-l+1)
  else:
    floor = (soma[r-1] - soma[l-2])//(r-l+1)

  print(floor)