palavras = []  #armazena as palavras descodificadas

#o código vai repetir 5 vezes
for i in range(1, 6):
    texto = input("Digite o nome da esfera: ")
    desloc = int(input("Digite o deslocamento: "))
    dia = int(input("Digite o número que condiz com o dia da semana: "))
    deslocamento = desloc + dia  #soma o deslocamento e o dia inseridos

    palavra = ""

    #vai passar por cada letra do texto digitado
    for i in texto:
        if i.isalpha():  #verifica se o caractere é uma letra
            codigo = ord(i)  #pega o a posição da letra
            codigo += (deslocamento % 26)  #muda o código da letra com o deslocamento (não deixa passar das letras do alfabeto)
            if i.isupper():  #se a letra for maiúscula
                if codigo > ord('Z'):  #se ultrapassar 'Z', volta para o começo do alfabeto
                    codigo -= 26
                elif codigo < ord('A'):  #se for menor que 'A', volta para o fim do alfabeto
                    codigo += 26
            else:  #se a letra for minúscula
                if codigo > ord('z'):  #se ultrapassar 'z', volta para o começo do alfabeto
                    codigo -= 26
                elif codigo < ord('a'):  #se for menor que 'a', volta para o fim do alfabeto
                    codigo += 26
            palavra += chr(codigo)  #converte o código de volta para uma letra e adiciona na palavra final
        else:
            palavra += i  #se não for letra (como espaço ou pontuação), só adiciona na palavra

    palavras.append(palavra)  #adiciona a palavra descodificada na lista
    print(f"Palavra descodificada {i}: {palavra}")  #imprime a palavra descodificada da vez

#imprime todas as palavras descodificadas
print("Segredo de Sheng Long:")
for index, palavra in enumerate(palavras, 1):
    print(f"Palavra {index}: {palavra}")