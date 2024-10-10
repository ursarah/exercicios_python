while True:

    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o segundo numero: ')
    operador = input('Digite um operador \n[+]Soma\n[-]Subtração\n[*]Multiplicação\n[/]Divisão: ')
    numero_digitado = None
    operadores_permitidos = '+-*/'

    try:
        int_numero_1 = int(numero_1)
        int_numero_2 = int(numero_2)
        numero_digitado = True

        match operador:
            case '+':
                result = int_numero_1 + int_numero_2
                print(f'{int_numero_1}+{int_numero_2}={result}')
            case '-':
                result = int_numero_1 - int_numero_2
                print(f'{int_numero_1}-{int_numero_2}={result}')
            case '*':
                result = int_numero_1 * int_numero_2
                print(f'{int_numero_1}*{int_numero_2}={result}')
            case '/':
                result = int_numero_1 / int_numero_2
                print(f'{int_numero_1}/{int_numero_2}={result}')
    except:
        if numero_digitado is None:
            print('*=*'*10)
            print('Digite só numeros')
            print('*=*'*10)
            continue

    if operador not in operadores_permitidos:
        print('*=*'*10)
        print('Digite operador valido')
        print('*=*'*10)
        continue

    if len(operador) > 1:
        print('*=*'*10)
        print('Digite apenas um operador')
        print('*=*'*10)



    sair = input('Quer sair?[S/N] ')
    if sair in 'Ss':
        break