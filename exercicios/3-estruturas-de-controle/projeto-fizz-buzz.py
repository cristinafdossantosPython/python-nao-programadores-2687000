# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"
#Daqui para baixo: anotações minhas
#range(12,31) = cria uma lista de 12 a 30 (o 31 não entra)
#indice = 0 para criar um contador para percorrer a lista e substituir os elementos
#loop for para passar por cada elemento da lista
lista_numerica = list(range(12,31))
print(lista_numerica)
indice = 0
for numero in lista_numerica:
  if numero %3 == 0 and numero %5 == 0:
    lista_numerica[indice]= 'FIZZBUZZ'
    #aqui foi trocada a linha 19 de If para ELIF, para acrescer nova condição com "and", deve ser primeiro na estrutura do código
  elif numero %3 == 0:
    lista_numerica[indice]= 'FIZZ'
  elif numero %5 == 0:
    lista_numerica[indice]= 'BUZZ'
  else: 
    lista_numerica[indice]= numero
   #para incrementar a cada execução do indice com FOR (passar próx. elemento): indice +=1 
    #indice +=1 para incrementar a cada execução do indice com FOR (passar próx. elemento):
  indice +=1
print(lista_numerica)
#cuidado com os espaçamentos do código, pois o Python é sensível a isso.



