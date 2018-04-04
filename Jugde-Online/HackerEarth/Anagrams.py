#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/

entry = int(input())

for i in range(entry):
  string1 = list(input())
  string2 = list(input())
  string1.sort()
  string2.sort()
  if len(string1) <= len(string2):
    stringMaior = string2
    stringMenor = string1
  else:
    stringMaior = string1
    stringMenor = string2
  count = 0
  while(len(stringMaior) > count):
    if stringMaior[count] in stringMenor:
      stringMenor.remove(stringMaior[count])
      stringMaior.remove(stringMaior[count])
    else:
      count += 1
  
  print(len(stringMenor) + len(stringMaior))