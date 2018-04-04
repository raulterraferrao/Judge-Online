def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

instancia = 0
while(True):
  try:
    flag = False
    dicionario = {}
    instancia += 1
    entradas = input()
    print("Instancia " + str(instancia))
    for cardapio in range(int(entradas)):
      pedido1, pedido2 = input().split()
      if pedido1[0] != '!':
        negacao = '!' + pedido1
        if negacao in dicionario:
          dicionario[negacao].append(pedido2)
        else:
          dicionario[negacao] = list()
          dicionario[negacao].append(pedido2)
      else:
        negacao = pedido1[1::1]
        if negacao in dicionario:
          dicionario[negacao].append(pedido2)
        else:
          dicionario[negacao] = list()
          dicionario[negacao].append(pedido2)
      if pedido2[0] != '!':
        negacao = '!' + pedido2
        if negacao in dicionario:
          dicionario[negacao].append(pedido1)
        else:
          dicionario[negacao] = list()
          dicionario[negacao].append(pedido1)
      else:
        negacao = pedido2[1::1]
        if negacao in dicionario:
          dicionario[negacao].append(pedido1)
        else:
          dicionario[negacao] = list()
          dicionario[negacao].append(pedido1)
    ##print(dicionario)
    for chave, lista in dicionario.items():
      if chave[0] == "!":
        negacao = chave[1::1]
        achou = find_path(dicionario, chave, negacao)
      else:
        negacao = "!" + chave
        achou = find_path(dicionario, chave, negacao)
      if(achou is not None):
        flag = True
        break
    if flag == True:
      print("nao")
    else:
      print("sim")
    ##print(dicionario)
    print()
      

  except EOFError:

    break;