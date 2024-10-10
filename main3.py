frase = 'Python é uma linguagem multiparadigma. Python foi criado por Guido Van Rossum'
print(frase)
letra = input('Digite a letra que voce quer contar: ').lower()
count_letra = i = 0
count_loop = 1

while True:
        if len(letra) > 1:
            print('Digite apenas uma letra')            
            letra = input('Digite a letra que voce quer contar: ').lower()
            continue

        if frase[i].lower() == letra:
            count_letra += 1

        if count_loop == len(frase):
            break
        
        i +=1
        count_loop +=1


print(f'Contem {count_letra} letras "{letra.upper()}" na frase')