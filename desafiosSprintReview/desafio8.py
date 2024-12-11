import json

#AGENDAR
def agendar():
    # Lê os dados do arquivo JSON
    with open("studio.json", "r") as arquivo:
        dados = json.load(arquivo)
    # Solicita os dados do agendamento
    numero = int(input("Digite o número do agendamento: "))
    nome = input("Digite seu nome: ")
    dia = int(input("Digite o dia desejado: "))
    hora = input("Digite o horário desejado: ")
    # Cria um novo registro com os dados informados
    novo_registro = {
        "Número": numero,
        "Nome": nome,
        "Dia": dia,
        "Horário": hora
    }

    # Adiciona o novo agendamento à lista
    dados.append(novo_registro)
    # Salva as informações de volta no arquivo
    with open("studio.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("Aula agendada!\n")

# Função para cancelar uma aula
def cancelar():
    # Lê os dados do arquivo JSON
    with open("studio.json", "r") as arquivo:
        dados = json.load(arquivo)

    # Solicita o número da aula a ser cancelada
    numero = int(input("Digite o número da aula que deseja excluir: "))
    excluir = None
    # Procura pela aula no arquivo e a remove se encontrada
    for i, item in enumerate(dados):
        if item.get("Número") == numero:
            excluir = i
            break
    # Verifica se a aula a ser excluída foi encontrada
    if excluir is not None:
        # Remove a aula da lista de dados
        excluido = dados.pop(excluir)
        # Abre o arquivo 'studio.json' para atualizar os dados
        with open("studio.json", "w") as arquivo:
            # Escreve os dados atualizados no arquivo JSON, com indentação para melhorar a leitura
            json.dump(dados, arquivo, indent=4)
        # Exibe uma mensagem informando que a aula foi cancelada com sucesso
        print(f"Aula com número {numero} foi cancelada com sucesso.\n")
    else:
        # Caso não tenha sido encontrada nenhuma aula com o número informado, exibe uma mensagem de erro
        print(f"Nenhuma aula com o número {numero} foi encontrada.\n")

# Função para rastrear o progresso do aluno
def rastrear_progresso():
    # Lê os dados do arquivo JSON
    with open("studio.json", "r") as arquivo:
        dados = json.load(arquivo)

    # Solicita o número do aluno para pesquisar seu progresso
    numero = int(input("Digite o número do aluno que deseja pesquisar: "))
    resultados = [item for item in dados if item.get("Número") == numero]
    # Verifica se foram encontrados resultados para o número do aluno
    if resultados:
        # Se houver resultados, exibe uma mensagem informando que o progresso foi encontrado
        print("Progresso do aluno encontrado:")
        # Para cada resultado (informações do aluno) nos resultados encontrados, imprime os detalhes
        for resultado in resultados:
            # Exibe o nome, dia e horário das aulas do aluno
            print(f"Nome: {resultado['Nome']} | Dia: {resultado['Dia']} | Horário: {resultado['Horário']}")
        # Exibe o número total de aulas que o aluno já participou
        print(f"O aluno já esteve presente em {len(resultados)} aulas.\n")
    else:
        # Se não houver resultados encontrados (ou seja, o número do aluno não existe), exibe uma mensagem de erro
        print("Nenhum aluno encontrado com esse número.\n")


# Função para oferecer uma aula especial
def oferecer_aula():
    resposta = input("Você deseja fazer uma aula especial? (s/n): ").strip().lower()
    if resposta == "s":
        agendar()  # Chama a função de agendar aula caso o usuário aceite
    else:
        print("Operação cancelada.\n")

# Função para gerenciar evento (exibe informações sobre o evento)
def gerenciar_evento():
    print("Retiro de Yoga")
    print("Data: 30/02/2024")
    print("Horário: Das 08:00 às 13:00")
    print("Local: Praça da Represa\n")

# Função principal para o menu de opções
def menu():
    while True:
        # Exibe o menu de opções para o usuário
        print("1 - Agendar Aula")
        print("2 - Cancelar Aula")
        print("3 - Rastrear Progresso")
        print("4 - Oferecer Aula")
        print("5 - Gerenciar Evento")
        print("6 - Sair")

        escolha = int(input("Escolha uma operação: "))

        # Chama a função correspondente com base na escolha do usuário
        if escolha == 1:
            agendar()
        elif escolha == 2:
            cancelar()
        elif escolha == 3:
            rastrear_progresso()
        elif escolha == 4:
            oferecer_aula()
        elif escolha == 5:
            gerenciar_evento()
        elif escolha == 6:
            break  # Encerra o programa
        else:
            print("Operação indisponível. Tente novamente.\n")
# Chama o menu principal
menu()