import csv # Importa o módulo CSV para manipulação de arquivos no formato .csv

"""
Abre o arquivo 'vendas.csv' em modo de leitura ("r")
# newline="" evita linhas em branco extras na leitura do CSV
# encoding="UTF-8" garante a leitura correta de acentos e caracteres especiais
"""

with open ("analise_vendas/vendas.csv","r",newline = "", encoding="UTF-8") as arquivo:
  leitor = csv.DictReader(arquivo)

  # DictReader já cria dicionários com base no cabeçalho do CSV
  print("Cabeçalho: ", leitor.fieldnames) # Mostra os nomes das colunas

  for linha in leitor:
    quantidade = int(linha["quantidade_vendida"])
    valor_unitario = float(linha["valor_unitario"])
    valor_total = float(linha["valor_total"])

    print(f"{linha["produto"]} - {linha["mes"]}: {quantidade} unidades, R${valor_total:.2f} ")