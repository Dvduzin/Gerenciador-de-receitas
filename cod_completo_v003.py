import random
pratos_por_pais = {}

def adicionar_prato(pratos_por_pais):
                try:
                    qnt = int(input("Quantos pratos você quer adicionar: "))
                    cont = 0
                    while cont < qnt:
                        nome = input("Escreva o nome do prato: ").title()
                        pais = input("Digite o país: ").title()
                        
                        if pais in pratos_por_pais:
                            pratos_por_pais[pais].append(nome)  
                        else:
                            pratos_por_pais[pais] = [nome]  
                        cont += 1
                except ValueError:
                    print("Entrada inválida")
while True:
    # menu para selecionar o que será feito
    menu = int(input("""\t 
Menu de ações:
[1] Adicionar prato
[2] Visualizar pratos cadastrados
[3] Modificar prato
[4] Remover prato
[5] Sugestão de receita aleatória
[6] Pesquisar por ingrediente
[7] Encerrar utilização     

O que deseja fazer: """))
    
    match menu:
        case 1:
            # isso fica dentro do caso 1
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

            file = open('F:/Vscode_cesar/Programação/projeto/pratos_adicionados.csv', 'w', encoding='utf8')
            file.write(f"{resultadosPratosPorPais}")
            file.close()
            # aqui termina o caso 1

        case 2:
            # aqui começa o caso 2
            pais = input("De que país você deseja ver a visualizar a lista de pratos:")
            for pais, pratos in pratos_por_pais.items():
                print(f"\n--- {pais} ---")
            for prato in pratos:
                print(prato)
            print()
            # incompleto
            file = open('F:/Vscode_cesar/Programação/projeto/pratos_adicionados.csv', 'r', encoding="utf8")
            for i in (file):
                file.read() 
            # aqui termina o caso 2

        case 4:
              # aqui começa o caso 4
            def deletar_prato(pratos_por_pais):
                pais = input("Digite o nome do país: ").title()
                prato = input("Digite o nome do prato que deseja excluir: ").title()
                if pais in pratos_por_pais and prato in pratos_por_pais[pais]:
                    pratos_por_pais[pais].remove(prato)
                    print("Prato excluído!")
                else:
                    print("Prato não encontrado.")

            deletar_prato(pratos_por_pais)        
                # aqui termina o caso 4

        case 5:
            # aqui começa o caso 5
            dic_receitas = {'Pizza' : 'Pré-aqueça o forno a 230°C.Estique a massa de pizza em uma forma untada.Espalhe o molho de tomate sobre a massa.Cubra com queijo mussarela e os ingredientes opcionais.Asse por 10-15 minutos, ou até que a massa esteja crocante e o queijo derretido.Retire do forno, corte em fatias e sirva.',
                    'Salada de Frutas':'Modo de preparo: Corte as frutas em pedaços pequenos e misture em uma tigela. Regue com um pouco de suco de laranja ou limão para dar um toque refrescante.',
                    'Sanduíche de Frango':'Modo de preparo: Misture o frango desfiado com a maionese. Espalhe a mistura sobre uma fatia de pão, adicione a cenoura ralada e algumas folhas de alface. Cubra com outra fatia de pão e sirva.' }

            lista = dic_receitas.items()
            lista_receitas = [f"{chave}: {valor}" for chave, valor in lista]
            receitas = ", ".join(lista_receitas)
            print(random.choice(lista_receitas))
            # aqui termina o caso 5
        
        case 7:
            # aqui começa 7
            break
        # aqui termina o 7