
instancia = 0
while(True):
  try:
    instancia += 1
    vetor = {}
    entradas = input()
    flag = False
    print("Instancia " + str(instancia))
    for cardapio in range(int(entradas)):
      pedido1, pedido2 = input().split()
      if(pedido1[0] == '!' and pedido2[0] == '!'):
        nomePedido1 = max(pedido1[1::1],pedido2[1::1])
        nomePedido2 = min(pedido1[1::1],pedido2[1::1])
        nomePedido = nomePedido1 + nomePedido2
        if nomePedido in vetor:       
          key = vetor[nomePedido]
          key[3] = 'v'
          vetor[nomePedido] = key 
        else:
          vetor[nomePedido] = list("fffv")
      if(pedido1[0] == '!' and pedido2[0] != '!'):
        nomePedido1 = max(pedido1[1::1],pedido2[0::1])
        nomePedido2 = min(pedido1[1::1],pedido2[0::1])
        nomePedido = nomePedido1 + nomePedido2
        if nomePedido in vetor:       
          key = vetor[nomePedido]
          if nomePedido1 == pedido1[1::1]:
            key[2] = 'v'
          else:
            key[1] = 'v'
          vetor[nomePedido] = key 
        else:
          if nomePedido1 == pedido1[1::1]:
            vetor[nomePedido] = list("ffvf")
          else:
            vetor[nomePedido] = list("fvff")
      if(pedido1[0] != '!' and pedido2[0] == '!'):
        nomePedido1 = max(pedido1[0::1],pedido2[1::1])
        nomePedido2 = min(pedido1[0::1],pedido2[1::1])
        nomePedido = nomePedido1 + nomePedido2
        if nomePedido in vetor:       
          key = vetor[nomePedido]
          if nomePedido1 == pedido1[0::1]:
            key[1] = 'v'
          else:
            key[2] = 'v'
          vetor[nomePedido] = key 
        else:
          if nomePedido1 == pedido1[0::1]:
            vetor[nomePedido] = list("fvff")
          else:
            vetor[nomePedido] = list("ffvf")
      if(pedido1[0] != '!' and pedido2[0] != '!'):
        nomePedido1 = max(pedido1[0::1],pedido2[0::1])
        nomePedido2 = min(pedido1[0::1],pedido2[0::1])
        nomePedido = nomePedido1 + nomePedido2
        if nomePedido in vetor:       
          key = vetor[nomePedido]
          key[0] = 'v'
          vetor[nomePedido] = key 
        else:
          vetor[nomePedido] = list("vfff")
      if(vetor[nomePedido] == list("vvvv")):
        flag = True
        print("nao\n")
        break;
    if flag == False :
      print("sim\n")
      
  except EOFError:

    break;