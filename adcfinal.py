case 1:
    def adicionar_prato():
        try:
            pratos_por_pais = {}
            receitas_ingredientes 
            nome = input("Escreva o nome do prato: ").title()
            pais = input("Digite o país: ").title()
            ingrediente = input(f"Escreva os ingredientes do prato {nome}:").title()
            receita = input(f"Escreva o modo de preparo do prato {nome}:").capitalize() 
            if pais in pratos_por_pais:
                pratos_por_pais[pais].append(nome)  
            else:
                pratos_por_pais[pais] = [n
            receitas_ingredientes[ingrediente] = [rece
            lista_pais_prato = pratos_por_pais.items()
            listaPratosPorPais = [f"{chave}:{', '.join(valor)}" for chave, valor in lista_pais_prato]
            resultadosPratosPorPais = ", ".join(listaPratosPorP
            lista_receita_ingrediente = receitas_ingredientes.items()
            listaReceitaIngrediente = [f"| {chave} / {(', '.join(valor))}" for chave, valor in lista_receita_ingredie
            with open(caminho_arquivo,mode='a',encoding="utf8") as arquivo_csv:
                     for informacao in listaPratosPorPais:
                          for info in listaReceitaIngrediente:
                            arquivo_csv.write(informacao+info+'\n')
        except ValueError:
            print("Entrada inváli
    adicionar_prato()