#dicionario que armazena todos os produtos e seus valores
produtos = {
    "Frango Shun" : {"Detalhes" : "(contém farofa recheada de queijo)", "Valor": 60.00},
    "Frango Misty" : {"Detalhes" : "(contém batatas e azeitonas)", "Valor": 80.00},
    "Frango Mime" : {"Detalhes" : "(contém pimenta biquinho e pequi)", "Valor": 89.00},
    "Frango Jabu" : {"Detalhes" : "(contém repolho roxo e cebolas roxa)", "Valor": 55.00},
    "Frango Saga" : {"Detalhes" : "Grande Mestre (pimenta calabresa, farofa tradicional e cogumelos)", "Valor": 100.00},
    "AssaFenix" : {"Detalhes" : "(tradicional sem recheio)", "Valor": 52.00},
    "Combo bronze" : {"Detalhes" : "(Frango Shun, Frango Jabu + Guaraná Jesus 2L)", "Valor" : 120.00},
    "Combo prata" : {"Detalhes" : "(Frango Misty + Frango Mime + 1L de BlueIce)", "Valor": 180.00},
    "Combo ouro" : {"Detalhes" : "(2 Frangos Saga Grande Mestre + 2 Garrafas de Campari)", "Valor": 300.00}
}

#loop para o progama continuar perguntandos se o usuario deseja realizar alma ação
while True:
    print("Bem vindo a rotisseria AsSa Fenix! Que pedido você deseja atender? ")
    escolha = int(input("1 - Listar produtos | 2 - Realizar venda | " #pergunta qual ação será realizada
                        "3 - Relatório de vendas | 4 - Sair "))
    if escolha == 1: #se o usuário digitar 1 o programa mostra os produtos
        print(produtos)
    elif escolha == 2: #se o usuario digitar 2 o programa inicia o processo de venda
        venda = (input("Qual produto será vendido? "))
        if venda in produtos: #se o produto digitado estiver no dicionário...
                quantidade = int(input(f"Quantos {venda} seram vendidos? ")) #pergunta a quantidade desejada
                total = quantidade * produtos[venda]["Valor"] #calcula o valor da venda
                print(f"Venda Realizada! Total: R${total: .2f}") #mostra o valor total
                print()

                import json
                with open("dados.json", "r") as arquivo:
                    dados = json.load(arquivo)
                dados.append(venda) #adiciona a venda em um arquivo json
                with open("dados.json", "w") as arquivo:
                    json.dump(dados, arquivo, indent=4)

        else: #caso o produto digitado nao esteja no dicionario
            print("Produto não encontrado.")
            print()
    elif escolha == 3: #se o usuário digitar 3...
        print(dados) #...o programa acessa o json e imprime os dados que estao lá
        print()

    elif escolha == 4: #se o usuario digitar 4 o programa para
        break