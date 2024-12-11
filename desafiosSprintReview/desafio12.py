# Função para desenhar o estado atual das torres
def desenharTorres(torres):
    altura = 5  # Define a altura das torres (número máximo de discos)
    larguraTorre = 11  # Define a largura máxima dos discos, considerando que o maior disco é de tamanho 11

    # Esse laço irá fazer as torres, desde a base até os discos
    for nivel in range(altura, 0, -1):  # Para cada nível, se inicia do topo (altura = 5), vai até 1, decrescendo de 1 em 1
        linha = ""  # Inicializa uma linha para desenhar todos os discos em uma linha

        # Esse laço desenha individualmente cada torre
        for torre in torres:
            if len(torre) >= nivel:  # Verifica se existe um disco neste nível da torre
                disco = torre[nivel - 1]  # Pega o disco que está neste nível, utiliza o -1 para pegar o índice certo
                espacos = (larguraTorre - (disco * 2 + 1)) // 2  # Calcula o número de espaços na esquerda para centralizar o disco
                linha += " " * espacos + "=" * (disco * 2 + 1) + " " * espacos  # Desenha o disco, centralizado
            else:
                linha += " " * larguraTorre  # Se não houver disco neste nível, desenha espaços em branco para manter a estrutura

        print(linha)  # Imprime a linha com os discos ou espaços em branco

    # Após imprimir todos os níveis, desenha a base das torres (linha de separação)
    print("-" * larguraTorre * 3)  # Linha de base das torres
    # Desenha o nome das torres, centralizando cada nome na largura da torre
    print("Torre 1".center(larguraTorre) + "Torre 2".center(larguraTorre) + "Torre 3".center(larguraTorre))


# Função para mover um disco de uma torre para outra
def moverDisco(torres, origem, destino):
    # Verifica se a torre de origem está vazia
    if not torres[origem - 1]:
        print("\nERRO: A Torre de origem está vazia. Escolha outra torre.")
        return False  # Se a torre de origem estiver vazia, não é possível mover

    # Verifica se o disco na torre de origem é maior do que o disco na torre de destino (se houver um disco na torre de destino)
    if torres[destino - 1] and torres[origem - 1][-1] > torres[destino - 1][-1]:
        print("\nERRO: Você não pode colocar um disco maior sobre um disco menor.")
        return False  # Se o disco na origem for maior, não é permitido mover

    # Move o disco da torre de origem para a torre de destino
    disco = torres[origem - 1].pop()  # Remove o disco do topo da torre de origem
    torres[destino - 1].append(disco)  # Adiciona o disco no topo da torre de destino
    return True  # A movimentação foi bem-sucedida


# Função principal que gerencia o jogo
def main():
    print("Regras da Torre de Hanói:")  # Imprime as regras do jogo
    print("1. Você só pode mover um disco por vez.")  # Regra: mover apenas um disco por vez
    print("2. Apenas o disco no topo pode ser movido.")  # Regra: mover o disco no topo
    print("3. Nenhum disco maior pode ser colocado sobre um menor.")  # Regra: não pode colocar disco maior sobre menor
    print("4. O objetivo é mover todos os discos para a Torre 3.\n")  # Objetivo do jogo

    # Inicializa as torres com 5 discos na primeira torre e as outras vazias
    torres = [[5, 4, 3, 2, 1], [], []]
    movimentos = 0  # Inicializa o contador de movimentos

    # Exibe o estado inicial das torres
    print("Estado inicial das torres:")
    desenharTorres(torres)  # Chama a função para desenhar o estado inicial das torres

    # Inicia o loop do jogo, que continua até que a Torre 3 tenha todos os discos
    while torres[2] != [5, 4, 3, 2, 1]:
        try:
            print("\nDigite sua jogada no formato 'origem destino' (exemplo: 1 3):")  # Instrução para o usuário
            jogada = input("Sua jogada: ").strip()  # Recebe a entrada do jogador e remove espaços extras
            origem, destino = map(int, jogada.split())  # Divide a entrada em dois números inteiros (origem e destino)

            # Verifica se os números de origem e destino estão dentro do intervalo permitido (1 a 3)
            if origem < 1 or origem > 3 or destino < 1 or destino > 3:
                print("\nERRO: As torres devem ser números entre 1 e 3.")
                continue  # Se a entrada estiver fora do intervalo, pede ao usuário para tentar novamente

            if origem == destino:  # Verifica se a origem e o destino são diferentes
                print("\nERRO: A torre de origem e destino devem ser diferentes.")
                continue  # Se as torres forem as mesmas, pede ao usuário para tentar novamente

            # Tenta mover o disco entre as torres
            if moverDisco(torres, origem, destino):
                movimentos += 1  # Se o movimento for válido, incrementa o contador de movimentos
                desenharTorres(torres)  # Desenha o novo estado das torres após o movimento

        except (ValueError):  # Captura qualquer erro de valor (caso a entrada não seja um número válido)
            print("\nERRO: Entrada inválida. Certifique-se de usar o formato 'origem destino'.")

    # Quando a Torre 3 tiver todos os discos, o jogo termina
    print(f"\nParabéns! Você completou o jogo em {movimentos} movimentos!")  # Exibe uma mensagem de vitória


# Verifica se o script está sendo executado diretamente (não importado)
main()  # Chama a função principal para iniciar o jogo