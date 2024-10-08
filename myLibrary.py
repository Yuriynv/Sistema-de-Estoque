import pandas as pd
from os import path

# cadastrar produtos

def cadastrar_produto():
    estoque = pd.read_csv("estoque.csv", sep=";", encoding="latin-1") # sempre leia os arquivos que a função utilizará em seu escopo
    
    # um novo produto é cadastrado e salvo como um dataframe e após isso é concatenado ao dataframe de estoque, caso já não exista
    
    novo_produto = {
      'codigo_produto': input("Digite o código do produto: "),
      'nome_produto': input("Digite o nome do produto: ").lower(),
      'quantidade_estoque': int(input("Digite a quantidade em estoque: ")),
      'preco_produto': float(input("Digite o preço por unidade: R$ ").replace(",", "."))
    }

    if novo_produto['codigo_produto'] in estoque['codigo_produto'].values:
      print("Produto já cadastrado.")
      return

    novo_produto_df = pd.DataFrame([novo_produto])
    estoque = pd.concat([estoque, novo_produto_df], ignore_index=True)

    return estoque.to_csv("estoque.csv", index=False, sep=";", encoding="latin-1") # sempre salve o arquivo modificado

# mostrar produtos

def mostrar_produtos():
    estoque = pd.read_csv("estoque.csv", sep=";", encoding="latin-1") # sempre leia os arquivos que a função utilizará em seu escopo
    colunas_selecionadas = estoque[['codigo_produto', 'nome_produto', 'preco_produto']]
    print(f'{colunas_selecionadas}\n')

# registrar venda

def registrar_venda():
    estoque = pd.read_csv("estoque.csv", sep=";", encoding="latin-1") # sempre leia os arquivos que a função utilizará em seu escopo

    mostrar_produtos()

    codigo_produto = input("Digite o código do produto: ").strip()

    estoque['codigo_produto'] = estoque['codigo_produto'].astype(str)

    if codigo_produto not in estoque['codigo_produto'].values:
        print('Produto não encontrado')
        return

    quantidade_vendida = int(input("Digite a quantidade vendida: "))
    if quantidade_vendida <= 0:
        print('Quantidade inválida')
        return
    elif quantidade_vendida > estoque[estoque['codigo_produto'] == codigo_produto]['quantidade_estoque'].values[0]:
        print('Quantidade em estoque insuficiente')
        print(f'Quantidade em estoque: {estoque[estoque["codigo_produto"] == codigo_produto]["quantidade_estoque"].values[0]}')
        return

    nome_produto = estoque[estoque['codigo_produto'] == codigo_produto]['nome_produto'].values[0]
    preco_produto = estoque[estoque['codigo_produto'] == codigo_produto]['preco_produto'].values[0]

    valor_total = preco_produto * quantidade_vendida

    venda = {
        'codigo_produto': [codigo_produto],
        'nome_produto': [nome_produto],
        'quantidade_vendida': [quantidade_vendida],
        'valor_total': [valor_total]
    }

    venda_df = pd.DataFrame(venda)

    estoque.loc[estoque['codigo_produto'] == codigo_produto, 'quantidade_estoque'] -= quantidade_vendida

    estoque.to_csv("estoque.csv", index=False, sep=";", encoding="latin-1") # sempre salve o arquivo modificado

    return venda_df.to_csv("vendas.csv", mode='a', header=not path.exists("vendas.csv"), index=False, sep=";", encoding="latin-1") # sempre salve o arquivo modificado

# gerar relatorio de estoque em formato (.txt)

def gerar_relatorio_estoque():
  estoque = pd.read_csv("estoque.csv", sep=";", encoding="latin-1") # sempre leia os arquivos que a função utilizará em seu escopo

  with open("relatorio_estoque.txt", "w", encoding="utf-8") as relatorio:
    relatorio.write("="*61 + "\n")
    relatorio.write("RELATÓRIO DE ESTOQUE\n")
    relatorio.write("="*61 + "\n")
    relatorio.write(f"{'Código do Produto':<20}{'Nome do Produto':<20}{'Quantidade em Estoque':<10}\n")
    relatorio.write("-"*61 + "\n")

    for index, row in estoque.iterrows():
      codigo = row['codigo_produto']
      nome = row['nome_produto'].capitalize()
      quantidade = row['quantidade_estoque']
            
      relatorio.write(f"{codigo:<20}{nome:<20}{quantidade:<10}\n")
        
    relatorio.write("="*61 + "\n")
    relatorio.write("Fim do relatório.\n")
  try:
    estoque = pd.read_csv("estoque.csv", sep=";", encoding="latin-1")

    with open("relatorio_estoque.txt", "w", encoding="utf-8") as file:
      file.write("Relatório de Estoque\n")
      file.write("====================\n\n")
      file.write("Código do Produto | Nome do Produto | Quantidade em Estoque\n")
      file.write("----------------------------------------------------------\n")

      for index, row in estoque.iterrows():
        file.write(f"{row['codigo_produto']} | {row['nome_produto']} | {row['quantidade_estoque']}\n")
    
  except Exception as e:
    print(f"Erro ao gerar relatório: {e}")

# menu de inicialização

def menu():
    while True:
        print("===== MENU =====")
        print("1. Cadastrar Produto")
        print("2. Mostrar Estoque")
        print("3. Registrar Venda")
        print("4. Gerar Relatório de Estoque")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            mostrar_produtos()
        elif opcao == '3':
            registrar_venda()
        elif opcao == '4':
            gerar_relatorio_estoque()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")