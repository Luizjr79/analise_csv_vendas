# Análise de CSV - Vendas de Loja

Este repositório contém um exercício de análise de dados em Python puro. 
O objetivo é ler, processar e analisar os dados de vendas de uma rede de lojas a partir de um arquivo CSV.

## Arquivo CSV

O arquivo `vendas_lojas.csv` contém as seguintes colunas:

- **produto**: nome do produto vendido
- **setor**: setor da loja (Eletrônicos, Vestuário, Móveis, etc.)
- **quantidade_vendida**: quantidade vendida do produto
- **valor_unitario**: preço unitário do produto
- **valor_total**: valor total da venda (quantidade * valor_unitario)
- **mes**: mês da venda

## Objetivos do exercício

1. Ler o CSV usando Python puro (sem Pandas)
2. Calcular a receita total
3. Agrupar vendas por setor
4. Identificar produtos mais vendidos e mais lucrativos
5. Exibir os resultados no terminal

## Como usar

1. Clone este repositório
2. Execute o arquivo Python principal (ex: `analise_vendas.py`)
3. Observe os resultados no terminal