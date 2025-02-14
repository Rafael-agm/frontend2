# Inicializando variáveis para os cálculos
maior_altura = float('-inf')
menor_altura = float('inf')
soma_altura_masculino = 0
num_masculino = 0
num_feminino = 0

# Solicitando os dados para 15 pessoas
for i in range(15):
    # Entrada dos dados
    altura = float(input(f"Digite a altura da pessoa {i + 1} em metros: "))
    genero = input(f"Digite o gênero da pessoa {i + 1} (M para Masculino, F para Feminino): ").strip().upper()
    
    # Validar gênero
    if genero not in ['M', 'F']:
        print("Gênero inválido! Por favor, insira 'M' para Masculino ou 'F' para Feminino.")
        continue
    
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
print(f'\nMaior altura: {maior_altura} metros')
print(f'Menor altura: {menor_altura} metros')
print(f'Média de altura do gênero Masculino: {media_altura_masculino:.2f} metros')
print(f'Número de pessoas do gênero Feminino: {num_feminino}')
