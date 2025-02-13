# Dados simulados de altura e gênero (Masculino = 'M', Feminino = 'F')
dados = [
    (1.75, 'M'),
    (1.80, 'M'),
    (1.60, 'F'),
    (1.65, 'M'),
    (1.55, 'F'),
    (1.70, 'F'),
    (1.85, 'M'),
    (1.78, 'M'),
    (1.90, 'F'),
    (1.62, 'M'),
    (1.68, 'M'),
    (1.72, 'F'),
    (1.59, 'M'),
    (1.64, 'F'),
    (1.80, 'M')
]

# Inicializando variáveis para os cálculos
maior_altura = float('-inf')
menor_altura = float('inf')
soma_altura_masculino = 0
num_masculino = 0
num_feminino = 0

# Processando os dados
for altura, genero in dados:
    # Maior e menor altura
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    
    # Cálculos para o gênero masculino
    if genero == 'M':
        soma_altura_masculino += altura
        num_masculino += 1
    elif genero == 'F':
        num_feminino += 1

# Calculando a média de altura para o gênero Masculino
media_altura_masculino = soma_altura_masculino / num_masculino if num_masculino > 0 else 0

# Exibindo os resultados
print(f'Maior altura: {maior_altura} metros')
print(f'Menor altura: {menor_altura} metros')
print(f'Média de altura do gênero Masculino: {media_altura_masculino:.2f} metros')
print(f'Número de pessoas do gênero Feminino: {num_feminino}')

