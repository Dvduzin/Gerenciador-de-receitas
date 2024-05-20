pratos_por_pais = {}

menu = int(input(""" 
[1] Adicionar prato
[2] Visualizar pratos cadastrados
[3] Modificar prato
[4] Remover prato
[5] Sugestão de receita aleatória
[6] Pesquisar por ingrediente     
"""))

match menu:
    case 1:
        def adicionar_prato(prato, pais):
            
            if pais in pratos_por_pais:  
                pratos_por_pais[pais].append(prato)
            else:        
                pratos_por_pais[pais] = [prato]
            file = open("F:/Vscode_cesar/Programação/projeto/pratos_adicionados.csv")
            file.write((pratos_por_pais))
            file.close()
            return pratos_por_pais
        
        qnt_pratos = int(input("Quantos pratos você deseja adicionar:"))
        for i in range (qnt_pratos):
            prato_adicionado = input("\nQual prato você deseja adicionar:")
            pais_do_prato = input("\nDe que pais é o seu prato:")
            adicionar_prato(prato_adicionado,pais_do_prato)

    case 2:
        pais = input("De que país você deseja ver a visualizar a lista de pratos:")
        for pais, pratos in pratos_por_pais.items():
            print(f"\n--- {pais} ---")
        for prato in pratos:
            print(prato)
        print()