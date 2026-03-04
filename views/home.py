import flet as ft
from flet import *
from flet_route import Params,Basket #Importation des classes Params et Basket pour la gestion des paramètres et des données partagées entre les vues.


def HomeView(page:ft.Page,params:Params,basket:Basket): #Cette fonction définit le contenu de la vue d'accueil.

#**********************Création des éléments de l'interface**********************
    btn = ft.ElevatedButton(text="Commencer !",
                            color=ft.colors.WHITE, 
                            bgcolor=ft.colors.BLUE_400, 
                            on_click=lambda _: page.go(f"/rec_view"))
    txt = ft.Text(
                """Préparez-vous à tester vos connaissances dans le domaine de l’informatique ,vous devrez répondre à cinq questions dans ce QCM, avec quatre suggestions pour chacune ou vous devrez choisir la réponse appropriée.""",
                max_lines=10,
                width=300,
                text_align="CENTER",
                color="#505050"
                )
    # Column et pour bien positionné les éléments
    col = ft.Column(
        [
        ft.Row(controls=[ft.Text("Bienvenue", 
                                 theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
                                 color=ft.colors.BLUE_900, 
                                 font_family="Consolas")],
                                 alignment=ft.MainAxisAlignment.CENTER,
                                 height=130),
        ft.Row([txt],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text(value="Si vous êtes prêt, cliquez sur Commencer!",color="#505050")],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn],alignment=ft.MainAxisAlignment.CENTER,height=120)
        ]
        )

    c1 = ft.Container(
        image_src="C:\\Users\\hp\\Desktop\\DRNmem\\views\\m.jpeg",
        image_fit="FIT_WIDTH",
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=300,
        height=400,
        border_radius=10
    )

    c2 = ft.Container(
        content=col,
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=355,
        height=400,
        border_radius=10,
    )
    c1.margin = margin.only(left=10)
    c1.padding=padding.only(left=10)
    Container1=ft.Container(
        content=ft.Column(
          controls=[
             Row(
                controls=[
                    c1,
                    c2
                ]
            )
        ],
        ),
        padding=0,
        margin=0,
        bgcolor=ft.colors.WHITE,
        width=700,
        height=420,
        border_radius=10,
    
    )
    Container1.border=ft.border.all(2,ft.colors.BLUE_400)
    Container1.margin=margin.only(left=20)
    container_principale= ft.Container(
        image_src="C:\\Users\\hp\\Desktop\\DRNmem\\views\\Design2.png", 
        image_fit="cover",
        content=ft.Column(
            controls=[
              Container1,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=0,
        margin=0,
        bgcolor=ft.colors.TRANSPARENT,
        width=780,  
        height=490,  
    )
 
    
    return ft.View(
        "/",
        controls=[
             container_principale,
        ]
    )