# Declarando bibliotecas, variáveis, vetores, e etc...

import os
os.system('cls')
import random

caminho_arquivo = 'C:\Projeto_Python\pratos_adicionados.csv'
caminho_arquivo_2 = 'C:\Projeto_Python/favoritos.csv'


dic_receitas = {'Pizza' : 'Pré-aqueça o forno a 230°C.Estique a massa de pizza em uma forma untada.Espalhe o molho de tomate sobre a massa.Cubra com queijo mussarela e os ingredientes opcionais.Asse por 10-15 minutos, ou até que a massa esteja crocante e o queijo derretido.Retire do forno, corte em fatias e sirva.','Salada de Frutas':'Modo de preparo: Corte as frutas em pedaços pequenos e misture em uma tigela. Regue com um pouco de suco de laranja ou limão para dar um toque refrescante.','Sanduíche de Frango':'Modo de preparo: Misture o frango desfiado com a maionese. Espalhe a mistura sobre uma fatia de pão, adicione a cenoura ralada e algumas folhas de alface. Cubra com outra fatia de pão e sirva.'}

# Menu e seleção de ação seguinte.

while True:
    try:
            menu = int(input("""\t 
        +=============================================+  
        ||            Menu de ações:                 ||
        ||                                           ||
        ||        [1] Adicionar prato                ||
        ||        [2] Visualizar todos os pratos     ||
        ||        [3] Modificar algum elemento       ||
        ||        [4] Remover prato                  ||
        ||        [5] Filtragem por país             ||
        ||        [6] Sugestão de receita aleatória  ||
        ||        [7] Adicionar aos favoritos        ||
        ||        [8] Sortear favorito               ||
        ||        [9] Visualizar favoritos           ||
        ||        [10] Remover favoritos             ||
        ||        [11] Encerrar utilização           ||
        +=============================================+                        

                O que deseja fazer: """))

            # Ações que irão acontecer de acordo com a escolha.

            match menu:
                case 1:
                        def adicionar_prato():
                            try:
                                pratos_por_pais = {}
                                receitas_ingredientes = {}


                                nome = input("Escreva o nome do prato: ").title()
                                pais = input("Digite o país: ").title()
                                ingrediente = input(f"Escreva os ingredientes do prato {nome}:").title()
                                receita = input(f"Escreva o modo de preparo do prato {nome}:").capitalize() 
                                if pais in pratos_por_pais:
                                    pratos_por_pais[pais].append(nome)  
                                else:
                                    pratos_por_pais[pais] = [nome]

                                receitas_ingredientes[ingrediente] = [receita]



                                lista_pais_prato = pratos_por_pais.items()
                                listaPratosPorPais = [f"{chave}:{', '.join(valor)}" for chave, valor in lista_pais_prato]
                                resultadosPratosPorPais = ", ".join(listaPratosPorPais)


                                lista_receita_ingrediente = receitas_ingredientes.items()
                                listaReceitaIngrediente = [f"| {chave} / {(', '.join(valor))}" for chave, valor in lista_receita_ingrediente]


                                with open(caminho_arquivo,mode='a',encoding="utf8") as arquivo_csv:
                                         for informacao in listaPratosPorPais:
                                              for info in listaReceitaIngrediente:
                                                arquivo_csv.write(informacao+info+'\n')
                            except ValueError:
                                print("Entrada inválida")

                        adicionar_prato()

                case 2:
                    def visualizar():
                        with open(caminho_arquivo, mode='r', encoding='utf8') as file:
                            for linha in file:
                                pais = linha[:linha.index(":")]
                                lista_de_pratos = (linha[linha.index(":")+1:]).split()

                                print(f"\n\t---{pais}---")
                                print(' '.join(lista_de_pratos))
                    visualizar()

                case 3:
                    def modifique():
                            antigo = input("Qual elemento deseja modificar? ").title()
                            novo = input(f"Qual elemento você deseja por no lugar de {antigo}? ").title()
                            arquivo = open(caminho_arquivo, 'r', encoding='utf8')
                            conteudo = arquivo.read()
                            conteudo_modificado = conteudo.replace(antigo, novo)
                            arquivo.close()
                            arquivo = open(caminho_arquivo, 'w', encoding='utf8')
                            arquivo.write(conteudo_modificado)
                            arquivo.close()

                    modifique()


                case 4:
                    def remover():
                        antigo = input("Qual prato você deseja deletar? ").title()
                        novo = ''
                        try:
                            with open(caminho_arquivo, mode='r', encoding='utf8') as file:
                                    for linha in file:
                                        prato = linha[linha.index(":")+1:linha.index("|")]
                                        if prato == antigo:
                                            arquivo = open(caminho_arquivo, 'r', encoding='utf8')
                                            conteudo = arquivo.read()
                                            conteudo_modificado = conteudo.replace(linha, novo)
                                            arquivo.close()
                                            arquivo = open(caminho_arquivo, 'w', encoding='utf8')
                                            arquivo.write(conteudo_modificado)
                                            arquivo.close()
                                            file.truncate()

                                    else: 
                                        print('\nPrato não encotrado')
                        except:
                            print( )
                    remover()        

                case 5:
                    def filtragem_pais():
                            cont = 0
                            pais_selecionado = input("Digite o país que você deseja procurar:").title()

                            with open(caminho_arquivo, mode='r', encoding='utf8') as file:
                                for linha in file:
                                    pais = linha[:linha.index(":")]
                                    lista_de_pratos = (linha[linha.index(":")+1:]).split()

                                    if pais == pais_selecionado:
                                        cont+=1
                                        print(f"\n---{pais}---")
                                        print(' '.join(lista_de_pratos))

                            if cont == 0:
                                print('Prato não encontrado')

                    filtragem_pais()

                case 6:
                    def aleatoriedade():
                        lista = dic_receitas.items()
                        lista_receitas = [f"{chave}: {valor}" for chave, valor in lista]
                        receitas = ", ".join(lista_receitas)
                        print('\n',random.choice(lista_receitas))

                    aleatoriedade()    

                case 7:
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

                case 8:
                    def random_receita():
                        with open(caminho_arquivo_2, 'r', encoding='utf8') as arquivo:
                            lista_favoritos = []

                            for linha in arquivo:  
                                    lista_favoritos.append(linha)
                            print('\n',random.choice(lista_favoritos))

                    random_receita()

                case 9:
                    def visualizar_favoritos():
                        with open(caminho_arquivo_2, mode='r', encoding='utf8') as file:
                            for linha in file:
                                pais = linha[:linha.index(":")]
                                lista_de_pratos = (linha[linha.index(":")+1:]).split()

                                print(f"\n\t---{pais}---")
                                print(' '.join(lista_de_pratos))
                    visualizar_favoritos()
                
                case 10:
                    def remover():
                        antigo = input("Qual prato você deseja deletar dos favoritos? ").title()
                        novo = ''
                        try:
                            with open(caminho_arquivo_2, mode='r', encoding='utf8') as file:
                                    for linha in file:
                                        prato = linha[linha.index(":")+1:linha.index("|")]
                                        if prato == antigo:
                                            arquivo = open(caminho_arquivo_2, 'r', encoding='utf8')
                                            conteudo = arquivo.read()
                                            conteudo_modificado = conteudo.replace(linha, novo)
                                            arquivo.close()
                                            arquivo = open(caminho_arquivo_2, 'w', encoding='utf8')
                                            arquivo.write(conteudo_modificado)
                                            arquivo.close()
                                            file.truncate()

                                    else: 
                                        print('\nPrato não encotrado')
                        except:
                            print( )
                    remover()
                
                case 11:
                      break
    except:
        print("Entrada inválida")