import pandas as pd
import myLibrary # importar minha biblioteca pessoal

# tabela inicial
dados = {
  'codigo_produto': ['1357', '2468', '1493', '8256'],
  'nome_produto': ['açúcar',  'arroz', 'café', 'feijão'],
  'quantidade_estoque': [10, 10, 10, 10],
  'preco_produto': [3.99, 6.49, 9.99, 6.99]
}

estoque = pd.DataFrame(dados)
estoque.to_csv("estoque.csv", index=False, sep=";", encoding="latin-1") # gerar (.csv) da tabela

# inicializar o código
if __name__ == "__main__":
  myLibrary.menu()