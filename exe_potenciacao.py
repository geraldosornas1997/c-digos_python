base = int(input(
    'insira o valor da base: '
    ))
e1 = int(input(
    f'insira o valor do expoente da base {base}: '
    ))

e2 = int(input(
    f'insira o valor do expoente da {base}: '
    ))
entrada_dados = input(
    'digite a operação:\n[M]Multiplicação \n[D]Divisão\n: '
    ).upper()

multiplicação = (e1+e2)
divisão = (e1-e2)
resultado = base ** multiplicação

if entrada_dados == 'M':
    print(
        f'{base}^{e1} x {base}^{e2}= {base}^{multiplicação}\nresultado da multiplicação:{resultado}'
        )

if entrada_dados == 'D':
    print(
        f'{base}^{e1} x {base}^{e2}= {base}^{divisão}\nresultado da multiplicação:{resultado}'
        )