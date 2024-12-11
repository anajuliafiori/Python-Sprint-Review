# Programa da Atividade da Torre
# O objetivo é calcular o tempo total para empilhar discos, considerando o tempo para cada tipo de disco.

# Função para verificar se todos os discos são válidos.
def verifica_discos(discos):
    erros = []
    for i in range(len(discos)):
        if not isinstance(discos[i], list):
            erros.append(f"Erro no disco {i}: valor '{discos[i]}' não é uma lista de inteiros.")
            continue
        for disco in discos[i]:
            if not isinstance(disco, int):
                erros.append(f"Erro no sub-disco {disco} da lista {i}: valor não é um inteiro.")
    if erros:
        for erro in erros:
            print(erro)
        return False
    return True

# Função para calcular o tempo total
def calcula_tempo_total(discos):
    total_time = 0
    for lista in discos:
        if type(lista) != list:
            print("Erro: Um dos elementos não é uma lista.")
        else:
            for disco in lista:
                if type(disco) != int:
                    print("Erro: Um dos discos não é um número inteiro.")
                else:
                    total_time = total_time + disco
    return total_time

# Função que recebe a lista de discos e define os tempos para cada tipo de disco.
def tempo_por_tipo(discos):
    tempo = {"grande": 5, "medio": 3, "pequeno": 1}
    for i in range(len(discos)):
        if not isinstance(discos[i], list):
            print(f"Erro: Elemento {i} não é uma lista.")
            continue
        else:
            for j in range(len(discos[i])):
                if discos[i][j] > 10:
                    discos[i][j] = tempo.get("grande", 5)
                elif discos[i][j] > 5:
                    discos[i][j] = tempo.get("medio", 3)
                else:
                    discos[i][j] = tempo.get("pequeno", 1)
    return discos


# Função que simula atrasos adicionais baseados em condições externas.
def calcula_atraso(total_time):
    atraso = 0
    if total_time > 20:
        atraso += 5
    elif total_time < 0:
        atraso = -1
    return atraso

# Função principal que inicia o programa.
def main():
    discos = [[12, 8, 7], [5, 3], [15, 6, 9]]

    if not verifica_discos(discos):
        print("Erro nos dados dos discos. Verifique e tente novamente.")
        return

    tempo_discos = tempo_por_tipo(discos)
    total_time = calcula_tempo_total(discos)


    if total_time is None:
        print("Erro: Não foi possível calcular o tempo total corretamente.")
        return

    atraso = calcula_atraso(total_time)

    if atraso == -1:
        print("Erro no cálculo do atraso.")
    else:
        total_time += atraso

    print("O tempo total para empilhar os discos é:", total_time)

# Chama a função principal
main()