from time import sleep   # Importa a função sleep para pausar a execução por um intervalo de tempo.

# Dicionário que armazena medicamentos e um valor booleano indicando se precisam de prescrição médica.
# True = Precisa | False = Não precisa
remedios = {
    "amoxicilina": True,
    "ibuprofeno": False,
    "paracetamol": False,
    "diazepam": True,
    "cetoconazol": True,
    "omeprazol": False,
    "simvastatina": True,
    "losartana": True
}

# Exibe uma mensagem de boas-vindas ao usuário.
print("===========================================")
print("Olá, Seja Bem-Vindo(a) a Farmácia PokeJoy!!")
print("===========================================\n")
sleep(1)  # Pausa de 1 segundo para melhorar a experiência do usuário.

# Função para verificar se um medicamento necessita de prescrição médica.
def verificar_prescricao(medicamento):
    # Converte o nome do medicamento para letras minúsculas e retorna o valor associado no dicionário.
    return remedios.get(medicamento.lower())

# Solicita ao usuário o nome do medicamento que deseja consultar.
medicamento = input("Digite o nome do medicamento para verificar se ele precisa de prescrição médica: ")
print("\nVerificando...")
sleep(1)  # Pausa de 1 segundo antes de exibir o resultado.

# Verifica se o medicamento precisa de prescrição médica usando a função definida anteriormente.
if verificar_prescricao(medicamento):
    # Exibe mensagem caso o medicamento exija prescrição.
    print(f"O medicamento {medicamento} REQUER prescrição médica.")
else:
    # Exibe mensagem caso o medicamento não exija prescrição.
    print(f"O medicamento {medicamento} NÃO REQUER prescrição médica.")
