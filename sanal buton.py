
#KOD EKLEYEN : MAHMUT ALTUNKANAT(Mat.Öğrt.)
#BU ÇALIŞMA; TİCARİ,YARIŞMA,REKLAM,KURS YADA PARA AMAÇLI DEĞİLDİR.SADECE HOBİ  NİYETLİ YAPILMIŞTIR.


#Tavsiye olarak python 3 ve üst sürümünü kullanın.
#ÖNEMLİ:PYTHON EN SON SÜRÜM KULLANIYORSANIZ opencv ve mediapipe kütüphanelerinin bir alt sürümünü kullanmanızı öneririm.
#Önce opencv,mediapipe,numpy  ve pyfirmata kütüphanelerini komut satırından pip install ile yükleyin.
#ArDuino kartına standart firmatayı yükledikten sonra python sayfası açık kalsın diğer programların sayfasını kapatabilirsiniz.Fakat arduino karta bağlı USB kablosunu çekmeyin
#NOT:python ile açılacak kamera görüntüsünün penceresinin size göre sol üst köşesinin başlangıç koordinatlarını (0,0) olarak alınır.


import cv2
import numpy


import mediapipe as mp
import pyfirmata

board=pyfirmata.Arduino('COM3')#ARDUİNO KARTININ BİLGİSAYARDA HANGİ COM A YANİ USB BÖLÜMÜNE BAĞLI  OLDUĞUNU BELİRTİR.SİZİN BİLGİSAYARANIZDA COM DEĞERİ FARKLI OLABİLİR.

kamera=cv2.VideoCapture(0)#WEBCAM KULLANIYORSANIZ DEĞERİ DEĞİŞTİRMEYİN.EĞER HARİCİ KAMERA KULLANIYORSANIZ PARANTEZİN İÇİNDEKİ DEĞERİ 1 YAPIN.
kamera.set(3,1200)#ekran pencere boyutu yatay(x ekseni):1200 
kamera.set(8,720)#ekran pencere boyutu dikey(y ekseni):720



a3=mp.solutions.hands

çizmek_=mp.solutions.drawing_utils




with a3.Hands(static_image_mode=True)as el_2:
    while True:
        
        _,frame=kamera.read()
        frame=cv2.flip(frame,1)#KAMERADAKİ EL İLE SİZİNİN ELİNİZ YÖNÜ TERS İSE DÜZELTMEK İÇİN FLİP KODU KULLANILIR.
        
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=el_2.process(rgb)
        yuk,gen,_=frame.shape#el hareketinde yükseklik ve genişlik algılama yerleri
        
        if result.multi_hand_landmarks:
            for çizmek_ in result.multi_hand_landmarks:
                for koordinat in a3.HandLandmark:
                    koordinat1=çizmek_.landmark[8]#işaret parmağı ucu 8 numaradır.
                    x=int(koordinat1.x*gen)
                    y=int(koordinat1.y*yuk)

                    cv2.circle(frame,(x,y),5,(0,255,0),-1)
                    if 430<=x<=660 and 30<=y<=120:
                        board.digital[6].write(1)
                        
                        
                        
                        
                        cv2.rectangle(frame,(430,30),(560,120),(0,0,255),-1)#dikdörtgenin sol üst köşe(başlangıç) koordinatları(430,30);bitiş sağ alt nokta koordinatları(560,120)
                        #el dikdörtgene değdiği zaman renk dolgusu için -1 değerini belirtiyorsunuz.
                    if 30<=x<=160 and 30<=y<=120:
                        board.digital[3].write(1)#arduinoda 3 numaralı pine bağlı led yanar
                        
                        
                        
                        cv2.rectangle(frame,(30,30),(160,120),(0,255,0),-1)#-1 SAYISI KUTUNUN İÇİNDEKİ RENK DOLGUSUNU BELİRLER.
                        
                        
                        
                       
                        
                        
                    
                    if 30<=x<=160 and 220<=y<=310:#parmak ucunun pencerede yatayda 30 ile 60 arasında dikeyde ise 220 ile 310 arasında olan  bölgede olması
                        board.digital[4].write(0)#arduinoda 4 numaralı pine bağlı led yanar
                        
                        
                        
                        
                        cv2.rectangle(frame,(30,220),(160,310),(255,0,0),-1)
                        
                        
                        
                        
                        
                        
                    if 430<=x<=660 and 220<=y<=310:
                        
                        board.digital[5].write(1)#arduinoda 5 numaralı pine bağlı led yanar
                        
                        
                        
                        
                        
                        cv2.rectangle(frame,(430,220),(560,310),(0,255,255),-1) #-1 RENK DOLGUSUNU YAPAR.
                        
                        
                    
                        
                       
        
        
                        
            
                        
        cv2.putText(frame,'MAT',(30,20),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)#dikdörtenin üstündeki yazı
        cv2.rectangle(frame,(30,30),(160,120),(0,255,0),2)#içi boş dikdörtgenlerin çerçevesin çizilmesi.
        cv2.putText(frame,'MAT1',(30,200),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        cv2.rectangle(frame,(30,220),(160,310),(255,0,0),2)
        cv2.putText(frame,'MAT2',(430,200),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),2)
        cv2.rectangle(frame,(430,220),(560,310),(0,255,255),2)
       
        cv2.rectangle(frame,(430,30),(560,120),(0,0,255),2)
        cv2.putText(frame,'MAT3',(420,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
        
        cv2.imshow('MATEMATIK ve YAPAY ZEKA',frame)#pencere başlığı.İsteyen burda başlığın penceredeki yerini korrdinat yazarak değiştirebilir.
        
        if cv2.waitKey(5)& 0xFF==ord('q'):#pencereyi q tuşuyla kapatma komutu
            break
kamera.release()
cv2.destroyAllWindows()
             
        
            
                

