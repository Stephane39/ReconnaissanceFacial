# Créé par Jay7, le 10/12/2022 en Python 3.7
import cv2
#insatncié des calassifiers qui détecte le visage
faceD = cv2.CascadeClassifier('face.xml')
profilD = cv2.CascadeClassifier('profileface.xml')
catD = cv2.CascadeClassifier('catface.xml')

cam=cv2.VideoCapture(0) #utiliser la cam
levier = 0

while (True): #la boucle est pour récupérer une vidéo
    #lire une image à partire de la cam qui sera stocké dans la variable img et status est un bolléan qui indique si on a pu lire l'image donc il est à true si non à flase
    status,img=cam.read()

    #Détecte des objets de différentes tailles dans l'image d'entrée. Les objets détectés sont renvoyés sous forme de liste de rectangles.
    faces = faceD.detectMultiScale(img,1.3,5)
    profil = profilD.detectMultiScale(img,1.3,5)
    cat = catD.detectMultiScale(img,1.3,5)

    #tracer le rectangle qui englobe le visage
    for x,y,w,h in profil:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    stop_cat = cv2.waitKey(1)
    if stop_cat == ord("c") or stop_cat == ("C"):
        print("pressure detected")
        if levier == 1:
            levier = 0
            print("cat off")
        elif levier == 0:
            print("cat on")
            levier = 1

    if levier == 1:
        for x,y,w,h in cat:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow("firstLive", img)
    #chaque 1ms un nouveau frame doit apparaitre
    stop = cv2.waitKey(1)
    # quand l'utilisateur click sur la touche z on va devoir fermer la frame qui souvre
    if stop == ord("Z") or stop == ord("z"):
        break

#supprime le frame cree
cv2.destroyWindow("firstLive")
#libirer la cam
cam.release()
