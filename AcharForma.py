import cv2
import numpy as np

def figName(contorno,width,height):
	epsilon = 0.01*cv2.arcLength(contorno,True)
	approx = cv2.approxPolyDP(contorno,epsilon,True)

	if len(approx) == 3:
		namefig = 'Triangulo'

	if len(approx) == 4:
		aspect_ratio = float(width)/height
		if aspect_ratio >= 0.8 and aspect_ratio <= 1.3  :
			namefig = 'Quadrado'
		else:
			namefig = 'Retangulo'

	if len(approx) == 5:
		namefig = 'Pentagono'

	if len(approx) == 6:
		namefig = 'Hexagono'

	if len(approx) > 10:
		namefig = 'Circulo'

	return namefig
#x=1
while True:  # para visualizar imagem
#while (x==1):# principal      
    frame = cv2.imread('ImagemTest1.png') #use esse ára usar uma imagem, definindo o camindo da mesma
    frame = frame[0:600, 15:800] #seleciona o tamonho da janela(crop)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.erode(threshold,kernel,iterations = 1)
    contours,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for (i,c) in enumerate(contours):
       (x,y,w,h) = cv2.boundingRect(c)
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)#da o contorno  na imagem
      
       name = figName(c,w,h)
       cv2.putText(frame,name,(x,y-5),1,0.8,(0,255,0),1)
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) #Recebe os valores digitados no teclado
    if key == 27:        #Se a tecla for a 27(ESC)
        break            #encerra

cv2.destroyAllWindows()
