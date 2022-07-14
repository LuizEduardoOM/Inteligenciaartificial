'''No aprendizado da árvore de decisão, o ID3 é um algoritmo inventado por Ross Quinlan usado para 
gerar uma árvore de decisão a partir de um conjunto de dados. O ID3 é o precursor do algoritmo C4.5 e 
geralmente é usado nos domínios de aprendizado de máquina e processamento de linguagem natural'''


#Bibliotecas Usadas
import pandas as pd                                 #para trabalhar com arquivos txt csv
from sklearn.model_selection import train_test_split#para separar aleatoriamente meus dados para evitar vicios
from sklearn.metrics import accuracy_score          #estabelecer um accuracy ou (porcentagem de acerto)
from sklearn.tree import DecisionTreeClassifier    #para classificar meu dados teste e treino
from sklearn.model_selection import cross_val_score #Para validar o meu modelo
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
import time


headers1 = ['FORMA','BASE','ALTURA','COR','CLASSE'] #cabeçalho geral de treino e teste
headers2 = ['FORMA','BASE','ALTURA','COR']          #cabeçalho da minha tabela de classificação 
dados_treino = 'treino.txt'                         #dados para aprendizado de maquina(machine learn)
dados_teste_real = 'dados_reais.txt'                      #Esses dados seram para um teste real
dados = pd.read_csv(dados_treino, sep=',', header=None, names=headers1) # recebe minha tabela
dados2 = pd.read_csv(dados_teste_real, sep=',', names=headers2)         #recebe minha tabela
dados.head() 


x = dados[["FORMA","BASE","ALTURA","COR"]] #Recebe minhas linhas e seus atributos
y = dados[["CLASSE"]]                      #Recebe minha coluna de classe

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size=0.2) # 40% dados de teste e 60% dados de treino 
modelo = DecisionTreeClassifier(criterion = 'entropy') #meu modelo = classificador de arvore de decisão entropy
modelo.fit(treino_x,treino_y)                          #faz um fit dos meus dados dentro do meu modelo e treina
previsoes = modelo.predict(teste_x)                    #prediz com os dados de teste

aux = modelo.predict(dados2)
print(f"Entropy:{aux}")
#time.sleep(2)
