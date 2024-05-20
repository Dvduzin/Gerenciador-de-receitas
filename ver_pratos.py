pratos_por_pais = {}

def adicionar_prato(prato, pais):
    if pais in pratos_por_pais:
        pratos_por_pais[pais].append(prato)
    else:
        pratos_por_pais[pais] = [prato]

qnt = int(input("Quantos pratos você deseja adicionar:"))
for i in range (qnt):
    prato_adicionado = input("\nQual prato você deseja adicionar:")
    pais_do_prato = input("\nDe que pais é o seu prato:")
    adicionar_prato(prato_adicionado,pais_do_prato)

for pais, pratos in pratos_por_pais.items():
    print(f"\n--- {pais} ---")
    for prato in pratos:
        print(prato)
    print()