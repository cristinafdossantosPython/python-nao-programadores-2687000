# Crie uma função para selecionar o curso desejado em uma trilha profissional
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
# Execute as funções
#Daqui para baixo: anotações minhas
#primeira função para selecionar o curso desejado em uma trilha profissional

def seleciona_curso_trilha():
    curso = int(
        input("Digite o número do curso desejado: 1 - Introdução ao SQL, 2 - Python para não programadores, 3 - Excel avançado: ")
    )
    return curso

#return para retornar o valor do curso selecionado para a função percorre_curso
#segunda função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual

def percorre_curso(curso_selecionado):
    trilha = {
        1: {'titulo': 'Introdução ao SQL', 'total_niveis': 5},
        2: {'titulo': 'Python para não programadores', 'total_niveis': 4},
        3: {'titulo': 'Excel avançado', 'total_niveis': 3},
    }

    curso_atual = trilha[curso_selecionado]['titulo']
    curso_nivel_atual = 1
    curso_total_niveis = trilha[curso_selecionado]['total_niveis']

    print(
        f'Bem vindo ao curso "{curso_atual}". Você está iniciando no nível {curso_nivel_atual}/{curso_total_niveis} níveis.'
    )

    while curso_nivel_atual <= curso_total_niveis:
        print(f'Parabéns, você concluiu a fase {curso_nivel_atual} do curso "{curso_atual}"')
        curso_nivel_atual += 1

    print(f'Parabéns, você concluiu o curso "{curso_atual}" com sucesso!')


curso = seleciona_curso_trilha()
percorre_curso(curso)
#curso para receber o valor retornado da função seleciona_curso_trilha 
#percorre_curso(curso) para executar a função percorre_curso com o valor do curso selecionado

