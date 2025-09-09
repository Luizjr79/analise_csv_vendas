import csv # Importa o módulo CSV para manipulação de arquivos no formato .csv

"""
Abre o arquivo 'vendas.csv' em modo de leitura ("r")
# newline="" evita linhas em branco extras na leitura do CSV
# encoding="UTF-8" garante a leitura correta de acentos e caracteres especiais
"""

with open ("analise_vendas/vendas.csv","r",newline = "", encoding="UTF-8") as arquivo:
  leitor = csv.reader(arquivo)

  cabecalho = next(leitor)
  print("Cabeçalho: ", cabecalho)

  for linha in leitor:
    print(linha)