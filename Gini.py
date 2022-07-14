#Bibliotecas Usadas
import pandas as pd                                 #para trabalhar com arquivos txt csv
from sklearn.model_selection import train_test_split#para separar aleatoriamente meus dados para evitar vicios
from sklearn.metrics import accuracy_score          #estabelecer um accuracy ou (porcentagem de acerto)
from sklearn.model_selection import cross_val_score #Para validar o meu modelo
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import time


headers1 = ['FORMA','BASE','ALTURA','COR','CLASSE'] #cabeçalho geral de treino e teste
headers2 = ['FORMA','BASE','ALTURA','COR']          #cabeçalho da minha tabela de classificação 
dados_treino = 'treino.txt'                         #dados para aprendizado de maquina(machine learn)
dados_teste_real = 'dados_reais.txt'                      #Esses dados seram para um teste real
dados = pd.read_csv(dados_treino, sep=',', header=None, names=headers1) # recebe minha tabela
dados2 = pd.read_csv(dados_teste_real, sep=',', names=headers2)         #recebe minha tabela


x = dados[["FORMA","BASE","ALTURA","COR"]] #Recebe minhas linhas e seus atributos
y = dados[["CLASSE"]]                      #Recebe minha coluna de classe

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size=0.2) # 40% dados de teste e 60% dados de treino 
modelo = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, class_weight=None,ccp_alpha=0.0)

modelo.fit(treino_x,treino_y)                         #faz um fit dos meus dados dentro do meu modelo e treina
previsoes = modelo.predict(teste_x)                   #prediz com os dados de teste


aux = modelo.predict(dados2)
print(f"Gini:{aux}")
#time.sleep(2)
