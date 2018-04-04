#http://br.spoj.com/problems/PLACAR/

instancia = 1
while True:
  minimo = 10
  reprovado = "zzzzzzzzzzzzzzzzz"

  try:
    alunos = int(input());
    for count in range(alunos):
      nome, questoes = input().split();
      questoes = int(questoes)
      if(questoes == minimo):
        reprovado = max(reprovado,nome)   
      if(questoes < minimo):
        reprovado = nome;
        minimo = questoes
    print("Instancia " + str(instancia))
    instancia +=1
    print(reprovado)
    print()
  except EOFError:
    break