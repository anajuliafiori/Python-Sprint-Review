from time import sleep  # Importa a função sleep para pausar a execução por um intervalo de tempo.

# Exibe uma mensagem de boas-vindas ao usuário.
print("=======================================")
print("Seja Bem-Vindo à Funerária HadesRules!!")
print("=======================================\n")
sleep(1)  # Pausa de 1 segundo

# Função que calcula o custo total do funeral com base em parâmetros fornecidos.
def calcular_custo_funeral(idade, caixao, querFlores):
    # Dicionário com os preços dos diferentes tipos de caixões.
    custoCaixao = {
        "simples": 500,
        "luxo": 1500,
        "premium": 3000
    }

    custo = 1000  # Custo base do funeral.
    custoIdade = 0  # Variável para armazenar o ajuste de preço com base na idade.

    # Ajusta o custo com base na idade do falecido.
    if idade < 18:
        custoIdade = -300  # Desconto para menores
    elif idade > 90:
        custoIdade = 700  # Acréscimo para pessoas idosas.

    custoFlores = 0  # Custo adicional para flores.
    if querFlores:
        custoFlores = 150  # Acrescenta o valor das flores caso a família as escolha.

    # Calcula o custo total somando os diferentes componentes.
    custoTotal = custo + custoIdade + custoCaixao.get(caixao.lower(), 0) + custoFlores
    return custoTotal

# Exibe a tabela de opções de caixões e seus valores.
print("==================================")
print("Tabela de caixões:")
print("PRODUTO | VALOR")
print("Simples | R$500")
print("Luxo    | R$1.500")
print("Premium | R$3.000")
print("==================================")
print("")
sleep(1)  # Pausa de 1 segundo para o usuário ler as informações.

# Solicita a entrada de dados ao usuário.
idade = int(input("Digite a idade do falecido: "))  # Idade do falecido.
caixao = input("Digite o tipo de caixão (simples, luxo, premium): ")  # Tipo de caixão escolhido.
# Verifica se a família deseja incluir flores. Converte a resposta para booleano.
querFlores = input("A família deseja incluir flores por R$150,00? (s/n): ").lower() == "s"

# Calcula o custo total do funeral usando a função definida anteriormente.
custo = calcular_custo_funeral(idade, caixao, querFlores)
print("\nCalculando...")
sleep(1)  # Pausa de 1 segundo antes de exibir o custo total.

# Exibe o custo total formatado com duas casas decimais.
print(f"O custo total do funeral é: R${custo:.2f}")
