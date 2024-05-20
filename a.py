def adicionar_prato(pratos_por_pais):
    try:
        pratos_por_pais = {}
        qnt = int(input("Quantos pratos você quer adicionar: "))
        cont = 0
        while cont < qnt:
            nome = input("Escreva o nome do prato: ")
            pais = input("Digite o país: ")
            
            if pais in pratos_por_pais:
                pratos_por_pais[pais].append(nome)  
            else:
                pratos_por_pais[pais] = [nome]  
            cont += 1
            return pratos_por_pais
    except ValueError:
        print("Entrada inválida")
