from datetime import date

# Obtendo a data atual
atual = date.today()
atual_lista = [atual.year, atual.month, atual.day]
print(atual_lista)

# Solicitando a data de nascimento do usuário
nascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
nascimento = nascimento.replace("/", " ").split()[::-1]
nascimento = [int(i) for i in nascimento]
print(nascimento)

def tempo(data_atual, data_nascimento):
    if (data_atual[1], data_atual[2]) < (data_nascimento[1], data_nascimento[2]):
        return data_atual[0] - data_nascimento[0] - 1
    else:
        return data_atual[0] - data_nascimento[0]

# Verifica se hoje é aniversário
if atual_lista[1] == nascimento[1] and atual_lista[2] == nascimento[2]:
    print("Feliz aniversário!")

idade = tempo(atual_lista, nascimento)
print("Você tem {} anos".format(idade))
