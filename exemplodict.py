
#criando o dicionario vazio alunos
alunos = {}

#criando a funcao para criar um dicionarios, pedindo para inserir dois imputs,
#nome e matricula
def incluir_aluno(alunos):
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite a matricula do aluno: ')
    #definindo que a matricula é a key e o nome é o item dentro do dicionario alunos
    alunos[matricula] = nome
    print('Aluno adicionado com sucesso!')

#criando a funcao que remove o aluno do dicionario alunos através de um for 
#acessando através da key "matricula", e tratando com um else se nao existir
def remover_aluno(alunos):
    matricula = ('Digite a matricula do aluno que deseja remover: ')
    if matricula in alunos:
        del alunos[matricula]
    else: print('Aluno não encontrado')

#criando a funcao de visualizar os alunos cadastrados, utilizando um for para percorrer
#os items inseridos no dicionario com o alunos.items()
def visualizar_alunos(alunos):
    for matricula, nome in alunos.items():
        print('Alunos cadastrados: \n'
              'Matricula:', matricula,
              '\nNome:', nome)
    if alunos == {}:
        print('Nenhum aluno adicionado ainda! \n')

## OPÇÕES DO USUÁRIO
#utilizando o while para o loop do menu do usuario e definindo o que fazer conforme
#o imput do usuario
while True:

    print('\nEscolha uma opção: ')
    print('1. Adicionar aluno')
    print('2. Remover aluno')
    print('3. Visualizar alunos')
    print('4. Sair')

    entrada_usuario = str(input('\nDigite a opção desejada: '))

    if entrada_usuario == '1':
        incluir_aluno(alunos)
    elif entrada_usuario == '2':
        remover_aluno(alunos)
    elif entrada_usuario == '3':
        visualizar_alunos(alunos)
    elif entrada_usuario == '4':
        print('Saindo do programa... ')
        break