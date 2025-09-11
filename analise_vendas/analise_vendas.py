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

  faturamento_total = 0
  faturamento_por_mes = {} # dicionário para guardar os valores por mês
  quantidade_vendas = {}

  for linha in leitor: # Convertendo os valores numéricos de string -> int
    quantidade = int(linha["quantidade_vendida"])
    valor_unitario = float(linha["valor_unitario"])
    valor_total = float(linha["valor_total"])
    mes = linha["mes"]
    produto = linha["produto"]

    if produto not in quantidade_vendas:
      quantidade_vendas[produto] = 0

    if mes not in faturamento_por_mes: # Se o mês ainda não está no dicionário, cria
      faturamento_por_mes[mes] = 0 

    # Acumula o valor no mês correspondente
    faturamento_por_mes[mes] += valor_total
    faturamento_total += valor_total # Soma o valor total ao acumulador
    quantidade_vendas[produto] += quantidade

    print(f"{linha['produto']} - {linha['mes']}: {quantidade} unidades, R$ {valor_total:.2f} ")

  # Ordem correta dos meses
  ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
  
  print("\n===== FATURAMENTO MENSAL =====")
  for mes in ordem_meses:
    if mes in faturamento_por_mes: # só imprime se o mês existe no CSV
       print(f"O faturamento do mes {mes} foi R$ {faturamento_por_mes[mes]:.2f}")

  # Descobrir o mês campeão de vendas
  mes_campeao = max(faturamento_por_mes, key=faturamento_por_mes.get)
  print(f"\nO mês de {mes_campeao} foi o campeão de faturamento, com R$ {faturamento_por_mes[mes_campeao]:.2f}")

  # Descobrir o mês com menor faturamento
  mes_pior = min(faturamento_por_mes, key=faturamento_por_mes.get)
  print(f"\nO mês de {mes_pior} apresentou o menor faturamento, com R$ {faturamento_por_mes[mes_pior]:.2f}")

  print("\n===== FATURAMENTO SEMESTRE =====")
  print(f"O faturamento total do semestre é R$ {faturamento_total:.2f}")

  # Descobrir o produto com maior quantidade de vendas  quantidade_vendida
  produto_campeao = max(quantidade_vendas, key=quantidade_vendas.get)
  print(f"\nO produto {produto_campeao} foi o mais vendido do semestre, com {quantidade_vendas[produto_campeao]} vendas")