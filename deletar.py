def deletar_prato(pratos_por_pais, file_name):
    pais = input("Digite o nome do país: ").title()
    prato = input("Digite o nome do prato que deseja excluir: ").title()

    if pais in pratos_por_pais and prato in pratos_por_pais[pais]:
        pratos_por_pais[pais].remove(prato)
        print("Prato excluído!")

        with open(file_name, 'w') as file:
            for pais, pratos in pratos_por_pais.items():
                file.write(f"{pais}: {';'.join(pratos)}\n")
    else:
        print("Prato não encontrado.")