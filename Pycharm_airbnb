"""
:autor = Lucas Rocha Vieira
"""
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

# csv sydney-austrália
df = pd.read_csv("http://data.insideairbnb.com/australia/nsw/sydney/2021-04-10/visualisations/listings.csv")


# Tratativa para mostrar todas as colunas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.head())

print("Linhas:\t {}\n".format(df.shape[0]) +  # Entrada
      "Colunas:\t {}\n".format(df.shape[1]))  # Variavel
print("-----------------------------------------\n")
display(df.dtypes)
print("-----------------------------------------\n")

# verificando a porcentagem de valores nulos em cada coluna
display((df.isnull().sum() / df.shape[0]).sort_values(ascending=False))
df.hist(bins=15, figsize=(20, 20));
plt.show()

# verificando os outlires nas colunas
print(df[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
          'calculated_host_listings_count', 'availability_365']].describe())

# minimum_nights
df.minimum_nights.plot(kind='box', vert=False, figsize=(15, 3))
plt.show()
plt.show()

# ver quantidade de valores acima de 30 dias para minimum_nights
print("minimum_nights: valores acima de 30:")
print("{} entradas".format(len(df[df.minimum_nights > 30])))
print("{:.4f}%".format((len(df[df.minimum_nights > 30]) / df.shape[0])*100))

# mostrar a quantidade de cada tipo de imóvel disponível
# price
df.price.plot(kind='box', vert=False, figsize=(15, 3),)
plt.show()

# ver quantidade de valores acima de 1500 para price
print("\nprice: valores acima de 1500")
print("{} entradas".format(len(df[df.price > 1500])))
print("{:.4f}%".format((len(df[df.price > 1500]) / df.shape[0])*100))

df.price.plot(kind='box', vert=False, xlim=(0, 1300), figsize=(15, 3));

# remover os *outliers* em um novo DataFrame
df_clean = df.copy()
df_clean.drop(df_clean[df_clean.price > 1500].index, axis=0, inplace=True)
df_clean.drop(df_clean[df_clean.minimum_nights > 30].index, axis=0, inplace=True)

# remover `neighbourhood_group`, pois está vazio
df_clean.drop('neighbourhood_group', axis=1, inplace=True)

# plotar o histograma para as variáveis numéricas
df_clean.hist(bins=15, figsize=(15, 10));
plt.show()

# criar uma matriz de correlação
corr = df_clean[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
                'calculated_host_listings_count', 'availability_365']].corr()
display(corr)
# hetmap
sns.heatmap(corr, cmap='RdBu', fmt='.2f', square=True, linecolor='white', annot=True)
plt.show()

# mostrar a quantidade de cada tipo de imóvel disponível
df_clean.room_type.value_counts()

# mostrar a porcentagem de cada tipo de imóvel disponível
df_clean.room_type.value_counts() / df_clean.shape[0]
var = df_clean.groupby(['neighbourhood']).price.mean().sort_values(ascending=False)[:10]

# plotar os imóveis pela latitude-longitude
df_clean.plot(kind="scatter", x='longitude', y='latitude', alpha=0.4, c=df_clean['price'], s=8,
              cmap=plt.get_cmap('jet'), figsize=(12, 8));

plt.show()
