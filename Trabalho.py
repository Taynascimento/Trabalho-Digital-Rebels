#3 ano DS
#Trabalho feito pelo grupo Digital Rebels
#Integrantes: Amanda, Gabriela, Laísa, Luísa, Sibelle, Taynara e Viviane.

import pandas as pd
import matplotlib.pyplot as plt

#Ler o arquivo CSV
df = pd.read_csv("vendas.csv")

#Mostrar as primeiras linhas do DataFrame 
print (df.head())

#total de vendas (Quantidade * Preço Unitário)
df['Total_Venda'] = df['Quantidade'] * df['Preço Unitário (R$)']

# Estastísticas básicas 
media_preco = df['Preço Unitário (R$)'].mean()
total_vendas = df['Total_Venda'].sum()
maior_venda = df['Total_Venda'].max()
menor_venda = df['Total_Venda'].min()

print(f"Média dos preços dos produtos:R$ {media_preco:.2f}")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Maior valor de venda R$ {maior_venda:.2f}")
print(f"Menor valor de venda: R$ {menor_venda:.2f}")

#Agrupar vendas por categoria
vendas_categoria = df.groupby('Categoria')["Total_Venda"].sum()

#Criar gráfico de barras
vendas_categoria.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor em R$')
plt.show()


# Total de vendas (Quantidade * Preço Unitário)
df['Total_Venda'] = df['Quantidade']* df['Preço Unitário (R$)']

# Estatíticas básicas
media_preco = df['Preço Unitário (R$)'].mean()
total_vendas = df['Total_Venda'].sum()
maior_venda = df['Total_Venda'].max()
menor_venda = df['Total_Venda'].min()

print(f"Média dos preços dos produtos: R$ {media_preco:.2f}")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Maior valor de venda: R$ {maior_venda:.2f}")
print(f"Menor valor de venda: R$ {menor_venda:.2f}")
