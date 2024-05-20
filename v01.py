pratos_por_pais = {}
ingredientes_por_prato = {}
lista_ingredientes = []
m = 0

def adicionar_prato(prato, pais):
    if pais in pratos_por_pais:
        pratos_por_pais[pais].append(prato)
    else:
        pratos_por_pais[pais] = [prato]
    
    
qnt_pratos = int(input("Quantos pratos você deseja adicionar:"))
for i in range (qnt_pratos):
    prato_adicionado = input("\nQual prato você deseja adicionar:")
    pais_do_prato = input("\nDe que pais é o seu prato:")
    adicionar_prato(prato_adicionado,pais_do_prato)


for pais, pratos in pratos_por_pais.items():
    print(f"\n--- {pais} ---")
    for prato in pratos:
        print(prato)
    print()


def adicionar_ingredientes(porIngredientes):
    ingredientes_por_prato[porIngredientes] = lista_ingredientes

porIngredientes = input("Qual prato você deseja por os ingredientes:")
qnt_ingredientes = int(input("Quantos ingredientes tem essa receita:"))

for n in range (qnt_ingredientes):
    
    ingredientes  = input(f"Qual o {n + 1}° ingrediente:")
    lista_ingredientes.append(ingredientes)
    adicionar_ingredientes(porIngredientes)

for pra, ings in ingredientes_por_prato.items():
    print(f"\n--- {pra} ---")
    for ing in lista_ingredientes:
        m += 1
        print(f" o {m}° ingrediente é {ing}")
    print()