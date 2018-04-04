#http://br.spoj.com/problems/CONTAGEM/
interacao = 1;
while True:
  try:
    palavra = input();
    count = 0;
    soma = 0;
    for i in range(len(palavra) - 1, -1, -1 ):
      if(palavra[i] == 'b'):
        soma += 2 ** count
      count += 1;
    print("Palavra " + str(interacao))
    print(soma)
    print()
    interacao += 1;
  except EOFError:
    break;