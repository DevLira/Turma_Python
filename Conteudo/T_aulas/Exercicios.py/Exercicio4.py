import random

n1 = str(input("Digite seu nome: "))
n2 = str(input("Digite seu nome: "))
n3 = str(input("Digite seu nome: "))
n4 = str(input("Digite seu nome: "))

lista = [n1, n2, n3, n4]

sorteado = random.choice(lista)

print("o nome sorteado foi {}! ".format(sorteado))
if sorteado == n1:
  print("primeiro da chamada")
elif sorteado == n2:
  print("segundo da chamada")
elif sorteado == n3:
  print("terceiro da chamada")
else:  
  print("quarto da chamada")