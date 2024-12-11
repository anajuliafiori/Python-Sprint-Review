def verificar_socios():
    # Lista de sócios do clube
    socios = ["Arthur Mambelli", "João Paulo", "Ana Julia", "Isabela Gonçalves"]

    # Coletando os nomes dos visitantes do cliente
    visitantes_input = input("Digite os nomes dos visitantes separados por vírgula: ")
    visitantes = [nome.strip() for nome in visitantes_input.split(",")]

    # Verificando quais visitantes são sócios
    socios_presentes = [nome for nome in visitantes if nome in socios]

    # Retornando a lista de sócios presentes
    return socios_presentes


# Exemplo de uso
if __name__ == '__main__':
    socios_encontrados = verificar_socios()
    print("Os seguintes visitantes são sócios do clube:", ", ".join(socios_encontrados))