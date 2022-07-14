import cv2
import numpy as np

#class AcharCor():
def figColor(imagenHSV):
        # Naranja
	brancoBaixo = np.array([0, 0, 255-15], np.uint8)
	brancoAlto = np.array([255, 15, 255], np.uint8)

	#Amarillo
	amareloBaixo = np.array([20, 100, 20], np.uint8)
	amareloAlto = np.array([32, 255, 255], np.uint8)

	#Verde
	verdeBaixo = np.array([36, 100, 20], np.uint8)
	verdeAlto = np.array([70, 255, 255], np.uint8)

	#Violeta
	vermelhoBaixo = np.array([160,20,70], np.uint8)
	vermelhoAlto = np.array([190,255,255], np.uint8)

	#Rosa
	azulBaixo = np.array([100,128,0], np.uint8)
	azulAlto = np.array([215,255,255], np.uint8)

	# Se buscan los colores en la imagen, segun los límites altos 
	# y bajos dados
	#maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
	#maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
	#maskRojo = cv2.add(maskRojo1, maskRojo2)
	maskBranco = cv2.inRange(imagenHSV, brancoBaixo, brancoAlto)
	maskAmarelo = cv2.inRange(imagenHSV, amareloBaixo, amareloAlto)
	maskVerde = cv2.inRange(imagenHSV, verdeBaixo, verdeAlto)
	maskVermelho = cv2.inRange(imagenHSV, vermelhoBaixo, vermelhoAlto)
	maskAzul = cv2.inRange(imagenHSV, azulBaixo, azulAlto)
	
	#cntsRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3	
	cntsBranco = cv2.findContours(maskBranco, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsAmarelo = cv2.findContours(maskAmarelo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsVermelho = cv2.findContours(maskVermelho, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsAzul = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3

	#if len(cntsRojo)>0: color = 'Rojo'
	if len(cntsBranco)>0: color = 'Branco'
	elif len(cntsAmarelo)>0: color = 'Amarelo'
	elif len(cntsVerde)>0: color = 'Verde'
	elif len(cntsVermelho)>0: color = 'Vermelho'
	elif len(cntsAzul)>0: color = 'Azul'

	return color
#x=1
while True:  # para visualizar imagem
#while (x==1):# principal
    frame = cv2.imread('ImagemTest1.png') #use esse ára usar uma imagem, definindo o camindo da mesma
    frame = frame[0:600, 15:800] #seleciona o tamonho da janela(crop)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 10,150)
    canny = cv2.dilate(canny,None,iterations=1)
    canny = cv2.erode(canny,None,iterations=1)
    cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #OpenCV 4
    imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for (i,c) in enumerate(cnts):
       (x,y,w,h)=cv2.boundingRect(c)
       #area= cv2.contourArea(c)
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)#da o contorno  na imagem
      # cv2.putText(frame,str(h),(x, y+h+13), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0, 255, 255),1)
       imAux = np.zeros(frame.shape[:2], dtype="uint8")
       imAux = cv2.drawContours(imAux, [c], -1, 255, -1)
       maskHSV = cv2.bitwise_and(imageHSV,imageHSV, mask=imAux)
       color = figColor(maskHSV)
       cv2.putText(frame,color,(x,y-5),1,0.8,(0,255,0),1)

    
    cv2.imshow("Frame", frame)
    #cv2.imshow("aa", canny) 
    key = cv2.waitKey(1) #Recebe os valores digitados no teclado
    if key == 27:        #Se a tecla for a 27(ESC)
        break            #encerra
cv2.imshow("Frame", frame)
cv2.destroyAllWindows()
    
