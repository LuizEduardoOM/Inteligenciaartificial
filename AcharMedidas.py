import cv2
import numpy as np

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
       (x,y,w,h)=cv2.boundingRect(c)
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)#da o contorno  na imagem
       cmx = round((w*1)/93,1) #tem que converter
       cmy = round((h*1)/87,1)

       cv2.putText(frame,str(float(cmx)),(x, y+h+13), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0, 255, 255),1)
       cv2.putText(frame, str(float(cmy)), (x+w+4, y+4), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0, 255, 255),1)
       cv2.putText(frame,str("(cm)"),(x, y+h+13+10), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0, 255, 255),1)
       cv2.putText(frame, str("(cm)"), (x+w+4, y+4+10), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0, 255, 255),1)
       base = cmx
       altura = cmy
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) #Recebe os valores digitados no teclado
    if key == 27:        #Se a tecla for a 27(ESC)
        break            #encerra

cv2.destroyAllWindows()
