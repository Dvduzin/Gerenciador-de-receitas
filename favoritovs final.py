caminho_arquivo = 'C:\Projeto_Python\pratos_adicionados.csv'
caminho_arquivo_2 = 'C:\Projeto_Python/favoritos.csv'
def favorito():
    cont = 0
    favoritar = input("Qual prato você quer favoritar: ").title()
    with open(caminho_arquivo, mode='r', encoding='utf8') as arquivo_entrada:
        for linha in arquivo_entrada:
            prato = linha[linha.index(":") + 1:linha.index("|")]
            if favoritar == prato:
                cont+=1
                with open(caminho_arquivo_2, 'a', encoding='utf8') as arquivo_saida:
                    arquivo_saida.write(linha)
    if cont == 1:                
        print("Prato adicionado à lista de favoritos")
    else:
        print("Prato não encontrado")
favorito()
