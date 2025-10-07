
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
