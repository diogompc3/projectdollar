#Bibliotecas em uso
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#Baixando os dados e os direcionando para uma variável
print("Baixando os dados...")
data_dollar = yf.download('BRL=X', period='2y')

#Primeiras linhas dos dados
print('\nPrimeiras linhas dos dados: ')
print(data_dollar.head())

#Criando e configurando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(data_dollar.index, data_dollar['Close'], color='green')
plt.title('Variação da Cotação do Dólar (BRL) - 2 Anos')
plt.xlabel('Data')
plt.ylabel('Valor do Dólar (R$)')
plt.grid(True)

#Exibição do gráfico
plt.show()
