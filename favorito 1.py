caminho_arquivo = 'pratos_adicionados.csv'

def favoritos():
    favorito = {}
    try:
        prato = input("Qual o prato que você quer favoritar: ")
        entrada = prato + ":"
    except ValueError:
        print("Entrada inválida")
    else:
        with open(caminho_arquivo, "r") as file:
            for linha in file:
                if entrada in linha:
                    receita = linha.strip().split(":")
                    ingredientes = receita[1].strip().split(",")
                    favorito[prato] = ingredientes
        print(favorito)

favoritos()