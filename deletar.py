def remover_prato():
    deletar=input("escreva o prato que você quer adicionar: ")
    with open('pratos_adicionados.csv','r',encoding='utf8')as file:
        linhas=file.readlines()
    with open('pratos_adiconados.csv','a',encoding='utf8') as file:
        for linha in linhas:
            linha.split(':','|')
            if deletar==linha[1]:
                linha=""
                print("prato deletado")
            else:
                print("prato não existente")    
remover_prato()                           