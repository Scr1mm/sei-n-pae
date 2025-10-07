Desafio 1

N = int(input())  # Número total de figurinhas no envelope
F = int(input())  # Número de amigos de João (excluindo João)
E = int(input())  # Número de figurinhas extras

# Cálculo do total de figurinhas
T = N + E

# Número total de partes: cada amigo recebe X, João recebe 2X, então total de partes = F * 1 + 1 * 2 = F + 2
partes = F + 2

# Cada amigo recebe X = T // partes (assumindo divisão exata, sem sobras)
X = T // partes

# João recebe 2 * X
joao_recebe = 2 * X

# Exibição do resultado
print(joao_recebe)

Desafio 2

# Assumindo que a entrada consiste em:
# - Primeira linha: número de alunos (A)
# - Segunda linha: número de monitores (M)
# Professores fixos: 8
A = int(input())  # Número de alunos
M = int(input())  # Número de monitores
# Cálculo do total de pessoas
professores = 8
total_pessoas = A + M + professores
# Capacidade máxima do bondinho
capacidade = 30
# Verificação se é possível em uma única viagem
if total_pessoas <= capacidade:
    print("SIM")
else:
    print("NAO")
