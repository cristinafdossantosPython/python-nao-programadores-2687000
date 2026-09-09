# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.
# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante ={}
estudante['nome'] = input('Qual é o seu nome?')
estudante['ano_cadastro_linkedin'] = int(input ('Em qual ano você cadastrou-se no Linkedin?'))
estudante['ano_atual'] = int(input ('Qual é o ano atual?'))
cursos = input('Informe os cursos concluídos na plataforma Linkedin Learning,separados por vírgula')
estudante['cursos'] = cursos.split(', ')

# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string , total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso
total_anos = estudante ['ano_atual']- estudante['ano_cadastro_linkedin']
total_cursos = len(estudante['cursos'])
print(f"Olá {estudante['nome']}, desde o ano {estudante['ano_cadastro_linkedin']} você conhece o Linkedin,são {total_anos} anos na plataforma, e você já completou {total_cursos} cursos, o primeiro curso foi {estudante['cursos'][0]} e o último foi {estudante['cursos'][-1]}.")                                                                                             