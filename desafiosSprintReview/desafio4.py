def calcular_desconto():
    # Pedindo o valor da total da compra
    valorTotal = float(input("Digite o valor total da compra: R$"))

    # Aplicando desconto de 15%
    valorDesc = valorTotal * 0.15

    # Calculando o valor total com desconto (85% do valor original)
    valorNovo = valorTotal * 0.85

    # Verificando se valor digitado é negativo ou 0
    if valorTotal <= 0:
        print("O valor não poder ser R$0,00 ou negativo!")  # Exibe mensagem caso o valor seja inválido
    else:
        # Exibe o valor original da compra
        print(f"Valor total da compra: R${valorTotal:.2f}")
        # Exibe o valor com o desconto aplicado
        print(f"Valor total com desconto: R${valorNovo:.2f}")
        # Exibe o valor do desconto ganho
        print(f"Desconto ganho: R${valorDesc:.2f}")


# Chamando a função para realizar o cálculo do desconto
calcular_desconto()