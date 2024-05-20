caminho_arquivo = 'C:\Projeto_Python\pratos_adicionados.csv'
def modifique():
        antigo = input("Qual elemento deseja modificar? ").title()
        novo = input(f"Qual elemento você deseja por no lugar de {antigo}? ").title()
        arquivo = open(caminho_arquivo, 'r', encoding='utf8')
        conteudo = arquivo.read()
        conteudo_modificado = conteudo.replace(antigo, novo)
        arquivo.close()
        arquivo = open(caminho_arquivo, 'w', encoding='utf8')
        arquivo.write(conteudo_modificado)
        arquivo.close
modifique()