base = 1
exp = 0
qtd_exp = 0
soma = 0
lista_expoente = []
expoente_multiplicado = 0
lista_multiplicada = []
def base_potenciacao():
    global base
    global exp
    base = int(input('digite o valor da base: '))
    exp = int(input('digite o valor do expoente: '))
    print(f'{base}^{exp}')

def calculo_de_potencia():
    calculo_potencia = (base**exp)
    print(calculo_potencia)

def calculo_de_multiplacao(expoente_multiplicado):
    global qtd_exp
    global quantidade_expoente
    global lista_multiplicada
    global soma
    quantidade_expoente = int(input('quantas vezes a base está sendo multiplicada? '))
    while qtd_exp != quantidade_expoente:
        expoente_multiplicado = int(input('digite o expoente: '))
        lista_expoente.append(expoente_multiplicado)
        for expoente in lista_expoente:
            soma = expoente+expoente


        qtd_exp = qtd_exp + 1
    print(soma)
    return lista_multiplicada




lista_resultante = calculo_de_multiplacao(expoente_multiplicado)
print(f'resultado: {lista_resultante}')
