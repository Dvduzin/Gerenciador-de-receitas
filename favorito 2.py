def favorito():

    favoritar=input("Qual prato você quer favoritar: ").capitalize()
    with open('pratos_adicionados.csv', mode='r', encoding='utf8') as file:
        for linha in file:
            prato = linha[linha.index(":")+1:linha.index("|")]
            if favoritar==prato:
                with open('favoritos.csv','a') as file:
                        file.write(linha+'\n')
                        print("prato adicionado á lista de favoritos")
            else:
                print("prato não encontrado")
favorito()                