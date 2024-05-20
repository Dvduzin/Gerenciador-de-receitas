# Declarando bibliotecas, variáveis, vetores, e etc...

import os
os.system('cls')
import random

pratos_por_pais = {}

caminho_arquivo = 'C:\Projeto Python\pratos_adicionados.csv'


dic_receitas = {'Pizza' : 'Pré-aqueça o forno a 230°C.Estique a massa de pizza em uma forma untada.Espalhe o molho de tomate sobre a massa.Cubra com queijo mussarela e os ingredientes opcionais.Asse por 10-15 minutos, ou até que a massa esteja crocante e o queijo derretido.Retire do forno, corte em fatias e sirva.',
'Salada de Frutas':'Modo de preparo: Corte as frutas em pedaços pequenos e misture em uma tigela. Regue com um pouco de suco de laranja ou limão para dar um toque refrescante.',
'Sanduíche de Frango':'Modo de preparo: Misture o frango desfiado com a maionese. Espalhe a mistura sobre uma fatia de pão, adicione a cenoura ralada e algumas folhas de alface. Cubra com outra fatia de pão e sirva.' }

# Função de adicionar pratos por país.

def adicionar_prato(pratos_por_pais):
    try:
        qnt = int(input("\nQuantos pratos você quer adicionar: "))
        cont = 0

        while cont < qnt:
            nome = input("\nEscreva o nome do prato: ").title()
            pais = input("\nDigite o país: ").title()

            cont = cont + 1
                        
            if pais in pratos_por_pais:
                pratos_por_pais[pais].append(nome)  
            else:
                pratos_por_pais[pais] = [nome]  

    except ValueError:
        print("\nEntrada inválida.\n")

# Menu e seleção de ação seguinte.

while True:

    menu = int(input("""\t 
Menu de ações:

[1] Adicionar prato
[2] Visualizar pratos cadastrados
[3] Modificar prato
[4] Remover prato
[5] Sugestão de receita aleatória
[6] Pesquisar por ingrediente
[7] Lista de favoritos
[8] Encerrar utilização                        

O que deseja fazer: """))
    
    # Ações que irão acontecer de acordo com a escolha.

    match menu:
        case 1:
            adicionar_prato(pratos_por_pais)

            for pais, pratos in pratos_por_pais.items():
                print(f"\n---{pais}---")
                for prato in pratos:
                    print(prato)
                print()

            lista_pais_prato = pratos_por_pais.items()
            listaPratosPorPais = [f"{chave}: {', '.join(valor)}" for chave, valor in lista_pais_prato]
            resultadosPratosPorPais = ", ".join(listaPratosPorPais)
            print(resultadosPratosPorPais)
            
            with open(caminho_arquivo, mode='a',encoding="utf8") as arquivo_csv:
                 for informacao in listaPratosPorPais:
                      arquivo_csv.write(informacao+'\n')

        case 2:
            caminho = 'C:\Projeto Python\pratos_adicionados.csv'

            pais_selecionado = input("Digite o país que você deseja procurar:\n")

            with open(caminho, mode='r') as file:
                for linha in file:
                    pais = linha[:linha.index(":")]
                    lista_de_pratos =(linha[linha.index(":")+1:]).split()
                    
                    if pais == pais_selecionado:
                        print(f"---{pais}---")
                        for i in lista_de_pratos:
                            print(i)
            

        case 3:

            escolha3 = input("\nqual prato você deseja modificar? ")

        case 4:

            def deletar_prato(pratos_por_pais, file):
                pais = input("Digite o nome do país: ").title()
                prato = input("Digite o nome do prato que deseja excluir: ").title()

                if pais in pratos_por_pais and prato in pratos_por_pais[pais]:
                    pratos_por_pais[pais].remove(prato)
                    print("Prato excluído!")

                    with open(caminho_arquivo, 'w', encoding="utf8") as file:
                        for pais, pratos in pratos_por_pais.items():
                            file.write(f"{pais}: {';'.join(pratos)}\n")
                else:
                    print("Prato não encontrado.")        

                deletar_prato(pratos_por_pais,file)

        case 5:
            lista = dic_receitas.items()
            lista_receitas = [f"{chave}: {valor}" for chave, valor in lista]
            receitas = ", ".join(lista_receitas)
            print(random.choice(lista_receitas))
        
        case 8:
            break