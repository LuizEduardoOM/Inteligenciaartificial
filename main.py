import sys

import AcharCor
import AcharForma
import AcharMedidas
#receber os dados
print(AcharCor.color)
print(AcharForma.name)
print(AcharMedidas.base)
print(AcharMedidas.altura)

base = AcharMedidas.base
altura = AcharMedidas.altura


if (AcharForma.name == "Quadrado"):
    forma = 1
if (AcharForma.name == "Circulo"):
    forma = 2
if (AcharForma.name == "Triangulo"):
    forma = 3
if (AcharForma.name == "Retangulo"):
    forma = 4
if (AcharForma.name == "Pentagono"):
    forma = 5
if (AcharForma.name == "Hexagono"):
    forma = 6
#---------------------------------------------
if (AcharCor.color == "Branco"):
    cor = 1
if (AcharCor.color == "Amarelo"):
    cor = 2
if (AcharCor.color == "Verde"):
    cor = 3
if (AcharCor.color == "Vermelho"):
    cor = 4
if (AcharCor.color == "Azul"):
    cor = 5
    
arq = open("dados_reais.txt","w+")
linhasParaOArquivo = ["Objt,",f"{forma},",f"{base},",f"{altura},",f"{cor}"]
for lnh in linhasParaOArquivo:
    arq.write(lnh)
    #arq.write("\n")
 
arq.close()
#print(novo.aux)
#mandar isso pro arquivo txt de teste
#executar o codigo da IA(classificação)

