import pandas as pd

# 1 - Arquivo do Excel

vendas = pd.read_excel('vendas_roupas.xlsx')
print(vendas)
print(30*'=')

# 2- 
vendas.head()
print(vendas.head(10))
print(30*'=')

# 3 -
total_vendas = pd.read_excel('vendas_roupas.xlsx')
total = vendas['Unidades Vendidas'].sum()
print(f'Soma total das vendas: {total}')
print(30*'=')

valor_medio = pd.read_excel('vendas_roupas.xlsx')
media = vendas['Preço por Unidade (R$)'].mean()
print(f'Preço medio é: {media:2f}')
print(30*'=')

faturamento = pd.read_excel('vendas_roupas.xlsx')
faturamento_total =vendas['Faturamento Total (R$)'].max()
print(f'Faturamento medio é: {faturamento_total}')
print(30*'=')

faturamento = pd.read_excel('vendas_roupas.xlsx')
faturamento_min = vendas['Faturamento Total (R$)'].min()
print(f'Faturamento minimo é: {faturamento_min}')
print(30*'=')

classificacao = pd.read_excel('vendas_roupas.xlsx')
produtos_baixa_satisfacao = vendas[vendas['Satisfação'] == 'Baixo']
print("Produtos com nível de satisfação baixo:")
print(produtos_baixa_satisfacao[['Produto', 'Satisfação']])