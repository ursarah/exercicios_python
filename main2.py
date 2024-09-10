"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_int = input("Digite um numero: ")

if '.' in numero_int:
    print("Não é um numero inteiro")
else:
    try:
        convert_numero_int = int(numero_int)
        
        if convert_numero_int%2==0:
            print("É um numero é par")
        else:
            print("É um numero é impar")
    except:
        print("Esse não é um numero")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    horario = input("Qual o seu horario? ")
    convert_horario_int = int(horario)

    if 0 <= convert_horario_int <= 11:
        print("Bom dia!!")
    elif 12 <= convert_horario_int <= 17:
        print("Boa tarde!!")
    elif 18 <= convert_horario_int <= 23:
        print("Boa noite!!")
    else:
        print("Digite um horario correto")
except:
    print("Digite numeros inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_user = input("Digite seu primeiro nome: ")

if len(nome_user) <= 4:
    print("Seu nome é curto")
elif 5 <= len(nome_user) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")