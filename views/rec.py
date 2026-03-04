import flet as ft
from flet import *
from flet_route import Params,Basket
import face_recognition  # Importation la bibliothèque face_recognition pour l'authentification
import cv2  # Importation la bibliothèque OpenCV 
import time 
from views.visages import encodages_visages_connus # Importation des encodages des visages connus
from views.visages import noms_visages_connus      # Importation des noms des visages connus

def RecView(page:ft.Page,params:Params,basket:Basket):


    t = 0
    fois = 0
    nom_utilisateur = ""

    def msj(VR,Nom):
            if VR: 
               ce.value='Identification réussie !'
               ce.font_family = "Verdana"
               ce.color = ft.colors.GREEN
               ce.opacity = 1
               ce.size = 20
               n = Nom
               c.image_src = "C:\\Users\\hp\\Desktop\\DRNmem\\views\\reussite.png"
               c.opacity = 1
               c.update()
               cc.value = "Vous pouvez maintenant accéder aux questions du quiz. Cliquez sur Commencer pour démarrer l'aventure."
               cc.size=13
               cc.max_lines=4
               cc.color = ft.colors.GREY
               cc.text_align ="CENTER"
               cn.value=Nom
               cn.weight = ft.FontWeight.W_500
               cn.text_align ="CENTER"
               cn.update()
               btn.disabled = False
               ce.update()
               cc.update()
               btn.update()
            #Sinon on informe l'utilisateur qu'il peut pas acceder et l'application vas s'arrete toute seule
            if not VR:
               ce.value="Erreur d'Identification"
               ce.font_family = "Verdana"
               ce.color = ft.colors.RED
               ce.size = 20
               cc.value="Désolé, nous n'avons pas pu vous identifier. Veuillez réessayer en vous assurant que votre visage est clairement visible et non masqué."
               cc.size=12
               cc.max_lines=6
               cc.font_family = "Verdana"
               cc.text_align ="CENTER"
               c.image_src = "C:\\Users\\hp\\Desktop\\DRNmem\\views\\erreu.png"
               c.update()
               cc.update()
               ce.update()
               time.sleep(5)
               page.window_destroy()
       

#Cette fonction est pour l'animation lors l'execution du processus de la reconnaissance
    def anim():
        c.opacity = 0 if c.opacity == 1 else 1
        ce.opacity = 0 if ce.opacity == 1 else 1
        c.update()
        ce.update()
        time.sleep(1)

#Cette fonction est la responsable d'effectuer la reconnaissance
    def reconnaissance(e):
        nonlocal t
        if t == 0 : 
            t = t+1
            video_capture = cv2.VideoCapture(0) #Lancer le capteur video
            ce.value='Identification en cours ...'
            ce.opacity = 0
            anim()
            visage_reconnu = False 
            nonlocal fois
            while (not visage_reconnu and fois<5) : #une boucle qui repete le processus 5 fois si aucun visage detecter
               nonlocal nom_utilisateur
               fois = fois + 1 #incrementer cette variable a chaque fois que ce processus se repete
               ret, frame = video_capture.read()  #Initialisation de la capture vidéo depuis la caméra
               anim()
               p_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) # Redimensionner l'image
               anim()
               rgb_frame = p_frame[:, :, ::-1] # Convertir l'image BGR vers RGB
               anim()
               localisation_visage = face_recognition.face_locations(rgb_frame) # Détecter les visages
               anim()
               encodages_visage = face_recognition.face_encodings(rgb_frame, localisation_visage)  # Encoder les visages détectés
               anim()
               for encodages_visage in encodages_visage:  # Parcourir chaque encodage de visage détecté
                correspandance = face_recognition.compare_faces(encodages_visages_connus, encodages_visage)  # Comparer aux visages connus
                nom = "Inconnu"
                anim()
                if True in correspandance : # Vérifier si une correspondance est trouvée
                    index_premiere_correspandance = correspandance.index(True) # Index de la première correspondance
                    anim()
                    nom = noms_visages_connus[index_premiere_correspandance] # Récupérer le nom du visage correspondant
                    visage_reconnu = True  # Indiquer qu'un visage a été reconnu
                anim()
            video_capture.release() # Libérer le périphérique de capture vidéo
            cv2.destroyAllWindows() # Fermer toutes les fenêtres OpenCV
            msj(visage_reconnu,nom) #Appel a la fonction qui vas mettre a jour l'interface
            
            

#**********************Création des éléments de l'interface**********************
    btn = ft.ElevatedButton(text="Commencer",
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE_400,
                            disabled=True,
                            on_click=lambda _: page.go(f"/qcm_view/{nom_utilisateur}")
                            )
    
    cb = ft.Container(content=btn,
                       padding=0,
                       margin=0,
                       width=150,
                       height=30,
                       )
    cb.margin = margin.only(left=580,top=-1)

    ce = ft.Text("Dans quelques instants, la reconnaissance faciale débutera.",
                 opacity=1,max_lines=2,size=15,width=300,text_align="CENTER",font_family = "Verdana")
    
    cc = ft.Text("",max_lines=2,width=300,font_family="Comic Sans MS")

    cn = ft.Text("",max_lines=2,width=300,font_family="Comic Sans MS")

    c = ft.Container(
                image_src="C:\\Users\\hp\\Desktop\\DRNmem\\views\\idr.png",
                image_fit="FIT_WIDTH",
                padding=0,
                margin=0,
                bgcolor=ft.colors.WHITE,
                width=240,
                height=240,
                border_radius=10,
                opacity=0
                )
    
    col = ft.Column(
        [
        ft.Row([ce],alignment=ft.MainAxisAlignment.CENTER,height=80),
        ft.Row([c],alignment=ft.MainAxisAlignment.CENTER,height=150),
        ft.Row([cn],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([cc],alignment=ft.MainAxisAlignment.CENTER)
        ]
    )

    txttt = ft.Text(value="Avant de commencer, nous devons vous identifier. Veuillez vous placer devant la caméra pour la reconnaissance faciale.",font_family = "Verdana",text_align ="CENTER",weight=ft.FontWeight.W_600,max_lines=6,size=14,width=300,height=350)
    
    cg = ft.Container(
        content=txttt,
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=600,
        height=50,
        border_radius=10,
    )
    cg.margin = margin.only(left=20)
    
    cd = ft.Container(
        content=col,
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=410,
        height=355,
        border_radius=10,
        on_hover=reconnaissance
    )
    cd.margin=margin.only(left=85)
    
    container2=ft.Container(
        content=ft.Column(
            controls=[
            cg,
            cd,
            ],
        ),
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=580,
        height=420,
        border_radius=10,
    )
    container2.margin=margin.only(left=90)
    container2.border=ft.border.all(2,ft.colors.BLUE_400)
    
    container_principale= ft.Container(
        image_src="C:\\Users\\hp\\Desktop\\DRNmem\\views\\rei.png", 
        image_fit="cover",
        content=ft.Column(
            controls=[
              container2,
              cb,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=0,
        margin=0,
        bgcolor=ft.colors.TRANSPARENT,
        width=780,  
        height=500,  
    )
    
    return ft.View(
        "/rec_view/id",
                controls=[container_principale]  
            )

