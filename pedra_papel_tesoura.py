import random

# Definindo os valores de início e fim do intervalo
inicio = 1
fim = 3
numero_sorteado = random.randint(inicio, fim)
# -- #

print("1) Pedra")
print("2) Papel")
print("3) Tesoura")
escolha = int(input("Escolha: "))

# Adicionando prints de depuração
print(f"Escolha do usuário: {escolha}")
print(f"Número sorteado: {numero_sorteado}")

if(numero_sorteado == escolha):
    print("Empate")
else:
    if numero_sorteado == 1:
        if escolha == 2:
            print("Parabéns, você ganhou!!")
        elif escolha == 3:
            print("Perdeu!!")
    elif numero_sorteado == 2:
        if escolha == 1:
            print("Perdeu!!")
        elif escolha == 3:
            print("Parabéns, você ganhou!!")
    elif numero_sorteado == 3:
        if escolha == 1:
            print("Parabéns, você ganhou!!")
        elif escolha == 2:
            print("Perdeu!!")
