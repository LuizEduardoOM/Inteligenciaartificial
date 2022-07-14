#Bibliotecas Usadas
from sklearn.dummy import DummyClassifier
import pandas as pd                                 #para trabalhar com arquivos txt csv
from sklearn.model_selection import train_test_split#para separar aleatoriamente meus dados para evitar vicios
from sklearn.metrics import accuracy_score          #estabelecer um accuracy ou (porcentagem de acerto)
from sklearn.model_selection import cross_val_score #Para validar o meu modelo
import time
headers1 = ['FORMA','BASE','ALTURA','COR','CLASSE'] #cabeçalho geral de treino e teste
headers2 = ['FORMA','BASE','ALTURA','COR']          #cabeçalho da minha tabela de classificação 
dados_treino = 'treino.txt'                         #dados para aprendizado de maquina(machine learn)
dados_teste_real = 'dados_reais.txt'                      #Esses dados seram para um teste real
dados = pd.read_csv(dados_treino, sep=',', header=None, names=headers1) # recebe minha tabela
dados2 = pd.read_csv(dados_teste_real, sep=',', names=headers2)         #recebe minha tabela

x = dados[["FORMA","BASE","ALTURA","COR"]] #Recebe minhas linhas e seus atributos
y = dados[["CLASSE"]]                      #Recebe minha coluna de classe
#while True:
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size=0.1) # 40% dados de teste e 60% dados de treino 
modelo = DummyClassifier(strategy="most_frequent")
modelo.fit(treino_x,treino_y)  
previsoes = modelo.predict(teste_x) 


aux = modelo.predict(dados2)
print(f"Dummy:{aux}-->Classificador 'burro'")
#time.sleep(1)
