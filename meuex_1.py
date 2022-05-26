# Vamos criar uma lista de compras e usar as funcoes de listas, interagindo com o usuario

from os import system


def menu():
  system('cls')
  print('1) primeira compra de fruta(funciona apenas uma vez)')
  print('2) alterar fruta')
  print('3) excluir fruta')
  print('4) deletar permanentemente a fruta')
  print('5) imprimir lista de frutas e lista de frutas excluidas')
  print('6) acrescentar fruta')
  print('0) sair do programa ')
  

def compras():
  system('cls')
  print('Para parar de comprar frutas basta da enter xD')
  fruta = 1
  while fruta != '':
    fruta = input('Olá amigo, vamos comprar frutas! me diga qual fruta você quer comprar: ')
    lista_compras_frutas.append(fruta)
  print('Suas frutas foram adicionadas na lista com sucesso. ') 
  for fruta in lista_compras_frutas:
    print(fruta)
  system('pause')
  


def alterar():
  system('cls')
  print('Essas são as frutas que temos na lista')
  for fruta in lista_compras_frutas:
    print(fruta)
  alterar_fruta = int(input('Agora vamos alterar uma fruta por outra fruta ok, Digite a posição da fruta que você quer alterar, exemplo: fruta 1 = 0,fruta 2 = 1, fruta 3 = 2... vamos lá: '))
  fruta_nova = input('Certo, agora nos diga qual a nova fruta você quer colocar: ')
  del lista_compras_frutas[alterar_fruta]
  lista_compras_frutas.insert(alterar_fruta,fruta_nova)
  print('Essa é a lista de frutas: ')
  for fruta in lista_compras_frutas:
    print(fruta)


def excluir():
  system('cls')
  print('Essas são as nossas frutas até o momento: ')
  for fruta in lista_compras_frutas:
    print(fruta)
  excluir_fruta = int(input('Vamos excluir uma fruta e deixar salva em uma lista de frutas excluidas, a posição da fruta, lembrando que começa na posição 0, digite: '))
  fruta_excluida = lista_compras_frutas.pop(excluir_fruta)
  frutas_excluidas.append(fruta_excluida)
  print('Essa é a lista de frutas excluidas ^^')
  for fruta in fruta_excluida:
    print(fruta)

def deletar():
  system('cls')
  print('Essa é a lista de frutas: ')
  for frutas in lista_compras_frutas:
    print(frutas)
  posicao = int(input('Vamos deletar uma fruta da lista permanentemente, Digite a posição da fruta que você quer excluir, exemplo: fruta 1 = 0,fruta 2 = 1, fruta 3 = 2... digite: '))
  del lista_compras_frutas[posicao]
  print('Fruta deletada, agora essa é a lista: ')
  for fruta in lista_compras_frutas:
    print(fruta)

def imprimir():
  system('cls')
  print('Essa é a lista de frutas')
  for fruta in lista_compras_frutas:
    print(fruta)
  if frutas_excluidas == []:
    print('A lista de frutas excluidas ainda está vázio.')
  else:
    print('Essa é a lista de frutas excluidas: ')
    for fruta in frutas_excluidas:
      print(fruta)
  system('pause')

def acrescentar():
  system('cls')
  fruta = input('Vamos adicionar na lista uma fruta agora, Digite o nome da fruta que quer inserir: ')
  lista_compras_frutas.insert(0,fruta)
  print('Fruta adicionada com sucesso')
  print('Essa é a lista de frutas nova: ')
  for fruta in lista_compras_frutas:
    print(fruta)

def main():
  system('cls')
  menu()
  number = int(input('Digite o número da alternativa: '))
  while number != 0:
    if number == 1:
      compras()
      menu()
      number = int(input('Digite o número da alternativa: '))

    elif number == 2:  
      alterar()
      menu()
      number = int(input('Digite o número da alternativa: '))

    elif number == 3:
      excluir()
      menu()
      number = int(input('Digite o número da alternativa: '))

    elif number == 4:
      deletar()
      menu()
      number = int(input('Digite o número da alternativa: '))

    elif number == 5:
      imprimir()
      menu()
      number = int(input('Digite o número da alternativa: '))

    elif number == 6:
      acrescentar()
      menu()
      number = int(input('Digite o número da alternativa: '))



lista_compras_frutas = [] 
frutas_excluidas = []
main()
print('Você saiu do programa até mais')