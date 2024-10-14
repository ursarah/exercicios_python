import os
lista_compras = []


while True:
    opcao = input('Digite uma opção\n[i]inserir\n[a]apagar\n[l]listar: ')

    if len(opcao) >1 or opcao not in 'ail':
        os.system('clear')
        print('Adicione só um valor ou o valor correto')
        continue

    if opcao == 'i':
        os.system('clear')
        item = input('Adicione um item: ')
        lista_compras.append(item)

    if opcao == 'a':
        os.system('clear')
        try:
            index = input('selecione um indice: ')
            lista_compras.pop(int(index))
        except IndexError:
            if lista_compras == []:
                print('A lista está vazia')
            else:
                print('Esse item não existe')

            continue
        except ValueError:
            print('Isso não é um indice')
            continue


    if opcao == 'l':
        os.system('clear')
        if lista_compras == []:
            print('Nada para listar')
            continue
        
        for index,item in enumerate(lista_compras):
            print(index,item)
    