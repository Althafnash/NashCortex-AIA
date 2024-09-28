import cv2
import winsound

def face():
    cam = cv2.VideoCapture(0) 
    while cam.isOpened(): 
        ret, frame1 = cam.read() 
        ret, frame2 = cam.read()

        width = int(cam.get(3))
        height = int(cam.get(4))

        font = cv2.FONT_HERSHEY_SIMPLEX  
        line = cv2.putText(frame1,"Althaf_Nash_Face_Detector",(10 , height - 10), font , 1 ,  (0,0,255),5 , cv2.LINE_AA)

        diff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray , (5,5) , 0 )
        _ , tresh = cv2.threshold(blur ,29 ,255 , cv2.THRESH_BINARY)
        dialated = cv2.dilate(tresh ,None , iterations=3)
        contorus , _ = cv2.findContours(dialated , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE )
        #cv2.drawContours(frame1 , contorus , -1 , (0 , 0 , 225) , 2)
        for c in contorus:
            if cv2.contourArea(c)  < 5000:
                continue
            x,y,h,w = cv2.boundingRect(c)
            cv2.rectangle(frame1 , (x,y),(x+w ,y+h),(0 , 0 , 225) , 2)
            winsound.Beep(500,200)
            print("Located")
        if cv2.waitKey(10) ==  ord('q'):
            break
        cv2.imshow('Face_Detector',frame1) 

