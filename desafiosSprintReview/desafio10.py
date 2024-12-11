from time import sleep # Importa o comando sleep (um intervalo de espera) da biblioteca time

('Olá, seja bem-vindo a academia MaiRRiro Acadimia! Aqui você encontra os melhores treinos com os melhores resultados!')
# Coleta informações sobre o usuário
peso = float(input("Para começar, digite o seu peso: "))
altura = float(input("Agora, digite a sua altura: "))
imc = peso / (altura ** 2) # Faz o cálculo do Índice Massa Corporal
print(f"Certo, de acordo com isso, o seu IMC é de: {imc:.2f}")

# Coleta outras informações sobre o usuário (essas serão inclusas nos cálculos)
percGordura = float(input("Para prosseguir, digite o seu percentual de gordura: "))
masMusc = float(input("Digite a sua massa muscular: "))
oxigenacao = float(input("Digite sua oxigenação: "))
freqCard = float(input("Digite sua frequência cardíaca: "))
focoMental = float(input("Digite o seu foco mental: "))

# Define o tempo de cada treino
tempoToguro = 200
tempoBaki = 300
tempoSaitama = 350
tempoJulin = 150
tempoCrackRRiani = 20
proporcao = 0 # Define um valor inicial para proporção, que será utilizado nos cálculos para proporção de horas treinadas

# Variáveis que guardam os aumentos/reduções dos treinos
aumentoMassaMuscular = 0
aumentoPercentualGordura = 0
aumentoFocoMental = 0
aumentoOxigenacao = 0
aumentoFreqCardiaca = 0

# Tabela apresentando todos os treinos e efeitos
print("Tudo bem, seus dados estão salvos em nosso sistema. Agora, serão apresentados os nossos treinos disponíveis: ")
sleep(3) # Intervalo de 3 segundos
print("")
print('===========================================================')
print('            Treino Toguro                           ')
print('- Aumento da Massa Muscular em 120%                 ')
print('- Redução do Percentual de Gordura em 20%           ')
print('- Aumento de 67% de Foco Mental                     ')
print('- Requer 200 horas de treino para o efeito completo ')
print('===========================================================')
print("")
sleep(1) # Intervalo de 1 segundo
print('===========================================================')
print('            Treino Baki                             ')
print('- Aumento da Massa Muscular em 70%                  ')
print('- Redução do Percentual de Gordura em 25%           ')
print('- Redução de 5% de Foco Mental                      ')
print('- Requer 300 horas de treino para o efeito completo ')
print('===========================================================')
print("")
sleep(1)
print('===========================================================')
print('            Treino Saitama                          ')
print('- Redução da Massa Muscular em 2%                   ')
print('- Aumento da Frequência Cardíaca em 5%              ')
print('- Redução do Percentual de Gordura em 75%           ')
print('- Requer 350 horas de treino para o efeito completo ')
print('===========================================================')
print("")
sleep(1)
print('===========================================================')
print('            Treino JulinNaQuebrada                  ')
print('- Aumento da Massa Muscular em 150%                 ')
print('- Redução do Percentual de Gordura em 30%           ')
print('- Redução da Oxigenação em 4%                       ')
print('- Requer 150 horas de treino para o efeito completo ')
print('===========================================================')
print("")
sleep(1)
print('===========================================================')
print('            Treino CrackRRiani                      ')
print('- Redução da Massa Muscular em 200%                 ')
print('- Redução do Percentual de Gordura em 45%           ')
print('- Redução da Oxigenação em 30%                      ')
print('- Aumento da Frequência Cardíaca em 60%             ')
print('- Requer apenas 20 horas de treino para o efeito completo')
print('===========================================================')
sleep(1)
print("")
# Opções para a pessoa decidir entre os treinos
print("Esses são todos os treinos disponíveis em nossa academia.")
print("1 - Treino Toguro")
print("2 - Treino Baki")
print("3 - Treino Saitama")
print("4 - Treino JulinNaQuebrada")
print("5 - Treino CrackRRiani")
print("")

while True:
    try: # O try irá testar se o dígito do usuário é inteiro, caso não, o except será mostrado
        treino = int(input("Digite o número respectivo do treino que deseja fazer: ")) # Solicita ao usuário o número do treino desejado
        tempo = int(input("Agora, digite o tempo, em horas, que você pode despender para os treinos: ")) # Solicita ao usuário a quantidade de horas que vai ter para os exercícios
        print("")
        if treino == 1: # Caso a pessoa selecione o primeiro treino
            print("O treino escolhido foi: Treino Toguro.")
            if tempo >= tempoToguro: # Caso o tempo digitado seja maior ou igual ao tempo necessário para o treino completo
                proporcao = tempo / tempoToguro # Realiza um cálculo para a proporção entre as horas digitadas e o tempo total
                aumentoMassaMuscular = 120 * proporcao # Os resultados do treino serão multiplicados pela proporção calculada
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100)) # Calcula a porcentagem de aumento com base no valor inicial digitado

                aumentoPercentualGordura = 20 * proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoFocoMental = 67 * proporcao
                focoMental = focoMental + (focoMental * (aumentoFocoMental / 100))

                # Exibe os resultados em porcentagem e novos valores após o treino
                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total de: {percGordura:.2f} de percentual de gordura.")
                print(f"Aumento do Foco Mental em: {aumentoFocoMental:.2f}%, resultando em um total de: {focoMental:.2f} de foco mental.")

            else: # Caso o tempo digitado seja menor que o treino completo necessita
                proporcao = tempoToguro / tempo # Realiza um cálculo para a proporção entre as horas digitadas e o tempo total
                aumentoMassaMuscular = 120 / proporcao # Os resultados do treino serão divididos (por ser menor) pela proporção calculada
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100)) # Calcula a porcentagem de aumento com base no valor inicial digitado

                aumentoPercentualGordura = 20 / proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoFocoMental = 67 / proporcao
                focoMental = focoMental + (focoMental * (aumentoFocoMental / 100))
                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total de: {percGordura:.2f} de percentual de gordura.")
                print(f"Aumento do Foco Mental em: {aumentoFocoMental:.2f}%, resultando em um total de: {focoMental:.2f} de foco mental.")

        elif treino == 2:
            if tempo >= tempoBaki:
                proporcao = tempo / tempoBaki
                aumentoMassaMuscular = 70 * proporcao
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100))

                aumentoPercentualGordura = 25 * proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoFocoMental = 5 * proporcao
                focoMental = focoMental - (focoMental * (aumentoFocoMental / 100))
                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(
                    f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total de: {percGordura:.2f} de percentual de gordura.")
                print(
                    f"Redução do Foco Mental em: {aumentoFocoMental:.2f}%, resultando em um total de: {focoMental:.2f} de foco mental.")

            else:
                proporcao = tempoBaki / tempo
                aumentoMassaMuscular = 70 / proporcao
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100))

                aumentoPercentualGordura = 25 / proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoFocoMental = 5 / proporcao
                focoMental = focoMental - (focoMental * (aumentoFocoMental / 100))

                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(
                    f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total de: {percGordura:.2f} de percentual de gordura.")
                print(
                    f"Redução do Foco Mental em: {aumentoFocoMental:.2f}%, resultando em um total de: {focoMental:.2f} de foco mental.")

        elif treino == 3:
            if tempo >= tempoSaitama:
                proporcao = tempo / tempoSaitama
                aumentoMassaMuscular = 2 * proporcao
                masMusc = masMusc - (masMusc * (aumentoMassaMuscular / 100))

                aumentoFreqCardiaca = 5 * proporcao
                freqCard = freqCard + (freqCard * (aumentoFreqCardiaca / 100))

                aumentoPercentualGordura = 75 * proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Redução da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(f"Aumento da Frequência Cardíaca em: {aumentoFreqCardiaca:.2f}%, resultando em um total de: {freqCard:.2f} de frequência cardíaca.")
                print(f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total: {percGordura:.2f} de percentual de gordura.")

            else:
                proporcao = tempoSaitama / tempo
                aumentoMassaMuscular = 2 / proporcao
                masMusc = masMusc - (masMusc * (aumentoMassaMuscular / 100))

                aumentoFreqCardiaca = 5 / proporcao
                freqCard = freqCard + (freqCard * (aumentoFreqCardiaca / 100))

                aumentoPercentualGordura = 75 / proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))
                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Redução da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(
                    f"Aumento da Frequência Cardíaca em: {aumentoFreqCardiaca:.2f}%, resultando em um total de: {freqCard:.2f} de frequência cardíaca.")
                print(
                    f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total: {percGordura:.2f} de percentual de gordura.")

        elif treino == 4:
            if tempo >= tempoJulin:
                proporcao = tempo / tempoJulin
                aumentoMassaMuscular = 150 * proporcao
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100))

                aumentoPercentualGordura = 30 * proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoOxigenacao = 4 * proporcao
                oxigenacao = oxigenacao - (oxigenacao * (aumentoOxigenacao / 100))

                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(
                    f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total: {percGordura:.2f} de percentual de gordura.")
                print(
                    f"Redução da Oxigenação em: {aumentoOxigenacao:.2f}%, resultando em um total: {oxigenacao:.2f} de oxigenação.")
            else:
                proporcao = tempoJulin / tempo
                aumentoMassaMuscular = 150 / proporcao
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100))

                aumentoPercentualGordura = 30 / proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoOxigenacao = 4 / proporcao
                oxigenacao = oxigenacao - (oxigenacao * (aumentoOxigenacao / 100))

                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(
                    f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total: {percGordura:.2f} de percentual de gordura.")
                print(
                    f"Redução da Oxigenação em: {aumentoOxigenacao:.2f}%, resultando em um total: {oxigenacao:.2f} de oxigenação.")

        elif treino == 5:
            if tempo >= tempoCrackRRiani:
                proporcao = tempo / tempoJulin
                aumentoMassaMuscular = 200 * proporcao
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100))

                aumentoPercentualGordura = 45 * proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoOxigenacao = 30 * proporcao
                oxigenacao = oxigenacao + (oxigenacao * (aumentoOxigenacao / 100))

                aumentoFreqCardiaca = 60 * proporcao
                freqCard = freqCard + (freqCard * (aumentoFreqCardiaca / 100))

                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(
                    f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total: {percGordura:.2f} de percentual de gordura.")
                print(
                    f"Redução da Oxigenação em: {aumentoOxigenacao:.2f}%, resultando em um total: {oxigenacao:.2f} de oxigenação.")
                print(
                    f"Aumento da Frequência Cardíaca em: {aumentoFreqCardiaca:.2f}%, resultando em um total: {freqCard:.2f} de frequência cardíaca.")
            else:
                proporcao = tempo / tempoJulin
                aumentoMassaMuscular = 200 / proporcao
                masMusc = masMusc + (masMusc * (aumentoMassaMuscular / 100))

                aumentoPercentualGordura = 45 / proporcao
                percGordura = percGordura - (percGordura * (aumentoPercentualGordura / 100))

                aumentoOxigenacao = 30 / proporcao
                oxigenacao = oxigenacao + (oxigenacao * (aumentoOxigenacao / 100))

                aumentoFreqCardiaca = 60 / proporcao
                freqCard = freqCard + (freqCard * (aumentoFreqCardiaca / 100))

                print(f"De acordo com as horas disponíveis: {tempo} horas")
                print("O efeito do treino será: ")
                print(
                    f"Aumento da Massa Muscular em: {aumentoMassaMuscular:.2f}%, resultando em um total de: {masMusc:.2f} de massa muscular.")
                print(
                    f"Redução do Percentual de Gordura em: {aumentoPercentualGordura:.2f}%, resultando em um total: {percGordura:.2f} de percentual de gordura.")
                print(
                    f"Redução da Oxigenação em: {aumentoOxigenacao:.2f}%, resultando em um total: {oxigenacao:.2f} de oxigenação.")
                print(
                    f"Aumento da Frequência Cardíaca em: {aumentoFreqCardiaca:.2f}%, resultando em um total: {freqCard:.2f} de frequência cardíaca.")

        # Condição para caso o usuário digite um número inválido
        else:
            print("Dígito inválido. Ocorreu um erro.")

        # Opção para o usuário continuar utilizando o programa
        print("\n1 - Para Calcular outro Treino")
        print("2 - Para sair")
        continuar = int(input("\nDeseja continuar a utilizar o programa? "))
        if continuar == 2:
            break
    # Caso o usuário digite um valor diferente de um número, o except mostrará o erro e continuará a repetir o código
    except (SyntaxError, ValueError):
        print("Dígito inválido. Tente novamente.")