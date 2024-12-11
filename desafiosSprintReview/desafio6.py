import random
from time import sleep


# Função para calcular o preço com desconto
def calcular_desconto(preco, desconto):
    return preco - (preco * desconto / 100)


# Função principal da campanha de prevenção
def campanha_prevencao():
    print("Bem-vindo á Campanha de Prevenção de Glaucoma!")
    pessoas = []  # Lista para armazenar os dados dos pacientes cadastrados

    while True:
        print("\nCADASTRO DE PACIENTE...")
        # Coletando dados do paciente
        nome = input("Nome: ").strip()
        sleep(1)  # Pausa para simular processamento
        idade = int(input("Idade: ").strip())
        sleep(1)
        sexo = input("Sexo (M/F): ").strip().upper()
        sleep(1)
        rg = input("RG: ").strip()
        sleep(1)
        telefone = input("Telefone: ").strip()
        sleep(1)
        email = input("Email: ").strip()
        print("Espere um momento...")
        sleep(3)  # Simulação de espera

        # Criando um dicionário para armazenar os dados do paciente
        pessoa = {
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
            "rg": rg,
            "telefone": telefone,
            "email": email
        }

        # Verificando a faixa etária do paciente para exames e benefícios
        if idade > 70:
            codigo = random.randint(10000, 99999)  # Gerando um código aleatório para exames
            print(f"\n{nome}, você tem mais de 70 anos e realizará os seguintes exames:")
            print("Glaucoma, Miopia, Fundo de Olho, Pressão Ocular e Perda Visual.")
            print(f"Seu código para exames é {codigo}.")

            # Calculando o preço com desconto para o benefício
            preco_com_desconto = calcular_desconto(10.99, 55.43)
            print(f"Você tem direito a 55,43% de desconto na garrafa de água ionizada RozanKoryuHa.")
            print(f"Preço com desconto: R${preco_com_desconto:.2f}.")

        elif idade > 50:
            codigo = random.randint(10000, 99999)  # Gerando um código aleatório para exames
            print(f"\n{nome}, você tem mais de 50 anos e realizará os seguintes exames:")
            print("Glaucoma, Miopia, Fundo de Olho.")
            print(f"Seu código para exames é {codigo}.")

            # Calculando o preço com desconto para o benefício
            preco_com_desconto = calcular_desconto(10.99, 55.43)
            print(f"Você tem direito a 55,43% de desconto na garrafa de água ionizada RozanKoryuHa.")
            print(f"Preço com desconto: R${preco_com_desconto:.2f}.")

        else:
            anos_faltantes = 50 - idade  # Calculando quantos anos faltam para atingir a idade mínima
            print(f"\n{nome}, você ainda não atingiu a idade mínima para os exames.")
            print(f"Por favor, retorne em {anos_faltantes} anos para realizar os exames.")

        # Adicionando os dados do paciente à lista
        pessoas.append(pessoa)

        # Perguntando se deseja cadastrar outra pessoa
        continuar = input("\nDeseja cadastrar outra pessoa? (S/N): ").strip().upper()
        if continuar != "S":
            break
    print("\nFim da campanha! Obrigado por participar.")


# Chamando a função principal para iniciar o programa
campanha_prevencao()