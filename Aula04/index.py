# Solicita ao usuário que insira o início e o fim do intervalo
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

# Inicializa a variável para armazenar a soma dos números pares
soma_pares = 0

# Itera sobre o intervalo usando um loop for
for numero in range(inicio, fim + 1):
    # Verifica se o número é par
    if numero % 2 == 0:
        # Se for par, adiciona à soma
        soma_pares += numero
# O else do for será executado se o loop terminar normalmente (sem break)
else:
    # Verifica se nenhum número par foi encontrado
    if soma_pares == 0:
        print("Não há números pares no intervalo especificado.")
    else:
        # Exibe a soma dos números pares
        print(f"A soma dos números pares no intervalo de {inicio} a {fim} é: {soma_pares}")
