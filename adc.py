


    case 1:
            def adicionar_prato():
                try:
                    pratos_por_pais = {}
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
                    print(pratos_por_pais)    

                    lista_pais_prato = pratos_por_pais.items()
                    listaPratosPorPais = [f"{chave}: {', '.join(valor)}" for chave, valor in lista_pais_prato]
                    resultadosPratosPorPais = ", ".join(listaPratosPorPais)
                    print(resultadosPratosPorPais)

                    with open(caminho_arquivo,mode='a',encoding="utf8") as arquivo_csv:
                             for informacao in listaPratosPorPais:
                                  arquivo_csv.write(informacao+'\n')
                except ValueError:                        
                     print("Entrada inválida")
                adicionar_prato()

        