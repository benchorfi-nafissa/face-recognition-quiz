import flet as ft
from flet import *
from flet_route import Params,Basket
from views.quiz import quiz

def QcmView(page:ft.Page,params:Params,basket:Basket):

# Récupération du nom de l'utilisateur depuis la fenêtre précédente
    nvnom = params.get("name") 

 # Initialisation des variables
    question_courrante = 0 # Index de la question courante
    score = 0  # Initialisation du score à 0
    selected_option = None  # Initialisation du choix sélectionné à None

#**********************Création des éléments de l'interface**********************
    t1 = ft.Text(value="Option 1", color=ft.colors.BLACK, height=20)
    t2 = ft.Text(value="Option 2", color=ft.colors.BLACK, height=20)
    t3 = ft.Text(value="Option 3", color=ft.colors.BLACK, height=20)
    t4 = ft.Text(value="Option 4", color=ft.colors.BLACK, height=20)

    r1 = ft.Radio(value=0, fill_color={ft.MaterialState.DEFAULT: ft.colors.BLUE})
    r2 = ft.Radio(value=1, fill_color={ft.MaterialState.DEFAULT: ft.colors.BLUE})
    r3 = ft.Radio(value=2, fill_color={ft.MaterialState.DEFAULT: ft.colors.BLUE})
    r4 = ft.Radio(value=3, fill_color={ft.MaterialState.DEFAULT: ft.colors.BLUE})

    btn = ft.ElevatedButton(text="Suivant",
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE_400,
                            on_click=lambda _: question_suivante(),
                            disabled=True)
    
    cb = ft.Container(
        content=btn,   
    )
    cb.margin=margin.only(right=30)

    Nom = ft.Text(value= nvnom , color=ft.colors.BLACK,font_family="Comic Sans MS")

    cg = ft.RadioGroup(content=ft.Column(
       controls=[
           ft.Row([r1, t1], alignment=ft.MainAxisAlignment.CENTER),
           ft.Row([r2, t2], alignment=ft.MainAxisAlignment.CENTER),
           ft.Row([r3, t3], alignment=ft.MainAxisAlignment.CENTER),
           ft.Row([r4, t4], alignment=ft.MainAxisAlignment.CENTER)
       ]
       ),on_change=lambda _:btn_Suivant())
    
    clg = ft.Column(
        [  
            ft.Row([cg],alignment=ft.MainAxisAlignment.CENTER, height=150),
        ]
    )

    tI = ft.Text(value="Veuillez selectionner la bonne reponse", color=ft.colors.GREY, font_family="Palatino Linotype")


    pb = ft.ProgressBar(width=790, value=0, height=8)
    pb.bgcolor=ft.colors.LIGHT_BLUE_100


    def dernier(e): # Fonction appelée lors du clic sur le bouton 'Resultat' à la dernière question
        cg_value = cg.value  # Récupération de la valeur du choix 
        if cg_value is not None:
            verifier_reponse(cg_value)  # Appeler la fonction qui vérifie la réponse
        e.page.go(f"/resultat_view/{score}/{nvnom}")  # Accéder à ResultatView

   

    def btn_Suivant():
        btn.disabled = False
        btn.update()

    def afficher_question(): # Fonction pour charger la question et ses propositions
        question = quiz[question_courrante] 
        choices = question['choice']
        t1.value = choices[0]
        t2.value = choices[1]
        t3.value = choices[2]
        t4.value = choices[3]
        cg.value = None
        return question["question"]

    def verifier_reponse(reponse_selectionne): # Fonction pour vérifier la réponse si elle est correcte
        question = quiz[question_courrante] 
        if reponse_selectionne == question["answer"]:  
            nonlocal score
            score = score + 10
            pb.value = pb.value + 0.2
            pb.update()

    def question_suivante():  # Fonction pour parcourir les questions et mettre à jour les éléments de l'interface
        cg_value = cg.value
        if cg_value is not None:
            verifier_reponse(cg_value)
        nonlocal question_courrante
        question_courrante = question_courrante + 1
        if question_courrante < len(quiz)-1 :
            new_question_text = afficher_question()
            cg.update()
            qst.value = new_question_text
            qst.update()
        else :
            new_question_text = afficher_question()
            cg.update()
            qst.value = new_question_text
            qst.update()
            btn.text = ("Resultat")
            btn.disabled = True 
            btn.on_click = dernier
            btn.update()

#**********************Création des contenaires pour bien positionne les elements**********************
    qst = ft.Text(value=afficher_question(), color=ft.colors.BLACK,size=15,weight=ft.FontWeight.W_600, font_family = "Verdana")
    cq = ft.Container(
        content=qst,
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=270,
        height=100,
        border_radius=10,
    )
    cq.margin=margin.only(left=10,top=50)
    
    co = ft.Container(
        content=clg,
        padding=0,
        margin=10,
        bgcolor=ft.colors.WHITE,
        width=250,
        height=180,
        border_radius=10
    )
    co.alignment = alignment.center
    co.margin=margin.only(top=50)
    co.border = ft.border.all(1, ft.colors.BLUE_400)

    ctG = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row([tI],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    controls=[cq, co],
                    alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([cb],alignment=ft.MainAxisAlignment.END),
                    ft.Row([Nom],alignment=ft.MainAxisAlignment.CENTER)
                ],alignment=MainAxisAlignment.START,
                ),
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=650,
        height=350,
        border_radius=10,
    )
    ctG.margin=margin.only(left=50,top=50)
    ctG.border = ft.border.all(2, ft.colors.BLUE_400)


    esp= ft.Container(
        image_src="C:\\Users\\hp\\Desktop\\DRNmem\\views\\rei.png", 
        image_fit="cover",
        content=ft.Column(
                controls=[pb,ctG]
            ,alignment=MainAxisAlignment.START,
        ),
        padding=0,
        margin=0,
        bgcolor=ft.colors.TRANSPARENT,
        width=990,  
        height=490
    )


    return ft.View(
        "/qcm_view/",
        controls=[esp]
    )
