from time import sleep  # Importa a função sleep para pausar a execução por um intervalo de tempo.

# Dicionário que armazena os produtos e seus respectivos preços.
produtos = {
    "cachorroquente": 12.50,
    "sucomagico": 7.50,
    "batataespecial": 17.00,
    "refridosdeuses": 9.40,
    "sanduichepy": 5.00
}

# Função que calcula o total do pedido com base nos itens selecionados.
def calcular_total_pedido(itensPedidos):
    total = sum(itensPedidos.values())  # Soma os valores de todos os itens no dicionário.
    return total

# Mensagem de boas-vindas.
print("================================")
print("Seja Bem-vindo a Cantina Makai!!")
print("================================\n")

sleep(1)  # Pausa por 1 segundo

# Exibe a tabela de produtos disponíveis no cardápio.
print("================================")
print("Tabela de produtos:             ")
print("PRODUTO        |           VALOR")
print("cachorroQuente |         R$12.50")
print("sucoMágico     |          R$7.50")
print("batataEspecial |         R$17.00")
print("refriDosDeuses |          R$9.40")
print("sanduíchePY    |          R$5.00")
print("================================")
print("")

# Dicionário para armazenar os itens pedidos pelo cliente.
itensPedidos = {}

# Loop principal para adicionar produtos ao pedido.
while True:
    # Solicita o nome do produto desejado.
    produto = input("\nDigite o nome do produto que deseja comprar (ou 'sair' para finalizar): ").lower() # Deixa todas as letras inseridas minusculas
    if produto == "sair":  # Verifica se o cliente deseja encerrar o pedido.
        break
    elif produto in produtos:  # Verifica se o produto está no cardápio.
        quantidade = int(input(f"Quantas unidades de {produto} você deseja? "))  # Solicita a quantidade.
        if produto in itensPedidos:
            # Adiciona a quantidade e o preço correspondente ao produto já existente no pedido.
            itensPedidos[produto] += produtos[produto] * quantidade
        else:
            # Adiciona o produto e o valor correspondente ao pedido.
            itensPedidos[produto] = produtos[produto] * quantidade
    else:
        # Mensagem de erro caso o produto não esteja no cardápio.
        print("Produto não encontrado no cardápio. Tente novamente.")

# Calcula o total do pedido usando a função definida anteriormente.
total = calcular_total_pedido(itensPedidos)
print("\nCalculando pedido...")
sleep(1)  # Pausa de 1 segundo antes de exibir o total.

# Exibe o total do pedido formatado com duas casas decimais.
print(f"Total do seu pedido: R${total:.2f}")
sleep(1)  # Pausa de 1 segundo antes da mensagem de agradecimento.
print("Muito obrigada por comprar na Cantina Makai!")
