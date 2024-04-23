base = 0
exp = 0
lista_expoente = []

def calculo_de_soma():
    global lista_expoente
    global soma
    global base
    base = int(input('base: '))
    quantidade_expoente = int(input('Quantas vezes a base está sendo somada? '))
    for _ in range(quantidade_expoente):
        expoente_somado = int(input('Digite o expoente: '))
        lista_expoente.append(expoente_somado)
    soma = sum(expoente for expoente in lista_expoente)
    return soma


resultado_soma = calculo_de_soma()
resultado_final = base ** resultado_soma
print(f'{base}^{resultado_soma} = {resultado_final}')

