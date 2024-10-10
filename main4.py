palavra_secreta = 'sarah'
letra_descoberta= ''
tentativas = 0

while True:
    letra_usuario = input('Digite uma letra: ')
    
    if len(letra_usuario) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_usuario in palavra_secreta:
        letra_descoberta += letra_usuario

        palavra_formada = '' 
        for ps in palavra_secreta:
            if ps in letra_descoberta:
                palavra_formada+= ps 
            else: 
                palavra_formada+='*'
                
        print(palavra_formada)

    if palavra_formada == palavra_secreta:
        break
    
    tentativas +=1

print(f'A palavra secreta é "{palavra_secreta}" e acertou em {tentativas} tentativas')