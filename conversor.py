'''
notação científica
a . 10^n 
1 <= a < 10
código que transforma um número em notação cientifica

'''
# verificar se o número é maior que dez
numero = float(input('digite a notação: '))
n = int(input('digite o expoente da base x10^ '))
formula_notacao = 10
contador_potencia = 0
contador_potencia_negativa = 0
print(f'{numero}x10^{n}')

if numero < 1:
    while numero < 1:
        mul = numero * 10
        numero = mul
        contador_potencia_negativa = contador_potencia_negativa - 1
        resultado = n - contador_potencia_negativa
    print(f'{numero}x10^{resultado}')

while numero > formula_notacao:
    div = numero / formula_notacao
    numero = div
    contador_potencia = contador_potencia + 1
    if numero < 1:
        print(n + contador_potencia)
    elif numero > 1 and numero < 10:
        print(f'{numero}x10^{n + contador_potencia}')

'''
se for menor que 1: ele foi divido por 1000 logo ele é 10³
ele tem que ser dividio por 100
se for maior que 1 e menor que 10 ele foi divido por 100 logo ele é 10²
'''



"""a1 = 12.6
a2 = 715
print(a1/10)
print(a2/100)"""
