# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
# Crie um while loop que imprima na tela o nível atual
# Insira "else" no while loop anterior.
#Daqui para baixo: anotações minhas
nivel_atual = 1
nivel_final = 5
while nivel_atual <= nivel_final:
  print(f'Você está no nível {nivel_atual}/{nivel_final}')
  nivel_atual += 1
else:
    print(f'Parabéns, você concluiu o curso!')

