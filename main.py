import flet as ft  # Importation la bibliothèque Flet pour construire l'interface web
from flet_route import Routing,path  #Importation des classes Routing et path pour gérer les routes.

#**********************Importation des différentes vues utilisées dans l'application**********************
from views.home import HomeView 
from views.rec import RecView 
from views.resultat import ResultatView 
from views.qcm import QcmView 

def main(page: ft.Page): #Cette fonction est le point d'entrée de l'application. Elle configure la page principale et le routage.

#**********************Définir les propriétés de la page principale**********************
    page.title = "QCM"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.window_height = 540
    page.window_width = 780
    page.bgcolor=ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment=ft.CrossAxisAlignment.START

#**********************Définir les routes de l'application**********************
    app_routes = [
        path(url="/",clear=True,view=HomeView ), 
        path(url="/rec_view", clear=True, view=RecView),
        path(url="/qcm_view/:name",clear=True,view=QcmView ),
        path(url="/resultat_view/:Rslt/:nom",clear=True,view=ResultatView )
    ]

#**********************Configurer le routage de l'application**********************
    Routing(
        page=page,
        app_routes=app_routes, 
        )
    
#**********************Naviguer vers la route actuelle**********************
    page.go(page.route)

ft.app(target=main) # Lancer l'application Flet avec la fonction main comme point d'entrée