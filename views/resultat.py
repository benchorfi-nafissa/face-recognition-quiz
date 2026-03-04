import asyncio
import flet as ft
from flet import *
from flet_route import Params,Basket




def ResultatView(page:ft.Page,params:Params,basket:Basket):

    #recuperation du nom de l'utilisateur et son score
    n = params.get("Rslt")
    k = params.get("nom")

#**********************Création des éléments de l'interface**********************
    p1 = ft.Text(value="", color=ft.colors.BLACK, weight=ft.FontWeight.W_900, size=45)
    p2 = ft.Text(value=k, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, size=20)
    p3 = ft.Text(value="Vous avez repondu sur ", color=ft.colors.BLACK , size=15)
    p4 = ft.Text(value="", size=25, weight=ft.FontWeight.W_600)
    p5 = ft.Text(value="/", size=25, weight=ft.FontWeight.W_600)
    p6 = ft.Text(value="5", size=25,weight=ft.FontWeight.W_600)
    p7 = ft.Text(value="bonnes réponses", color=ft.colors.BLACK , size=15)


# Fonction pour mettre à jour les éléments de l'interface
    def misjr(): 
        p2.update()
        p1.update()
        p4.update()
        p5.update()
        p6.update()

    # Fonction asynchrone pour afficher le résultat en fonction du score
    async def aff() :
        if(n == "0"):
            print("0")
            p1.value = "Malheuresement"
            p1.color = ft.colors.RED
            p4.value = "Aucune"
            p4.color = ft.colors.RED
            p5.value = ""
            p6.value = ""
            misjr
        elif(n == "10"):
            p1.value = "Malheuresement"
            p1.color = ft.colors.RED
            p4.value = "1"
            p4.color = ft.colors.RED
            p5.color = ft.colors.RED
            p6.color = ft.colors.RED
            misjr
        elif(n == "20"):
            p1.value = "Malheuresement"
            p1.color = ft.colors.RED
            p4.value = "2"
            p4.color = ft.colors.RED
            p5.color = ft.colors.RED
            p6.color = ft.colors.RED
            misjr
        elif(n == "50"):
            p1.value = "FELICITATION "
            p1.color = ft.colors.GREEN
            p4.value = "5"
            p4.color = ft.colors.GREEN
            p5.color = ft.colors.GREEN
            p6.color = ft.colors.GREEN
            misjr
        elif(n == "40"):
            p1.value = "FELICITATION "
            p1.color = ft.colors.GREEN
            p4.color = ft.colors.GREEN
            p4.value = "4"
            p5.color = ft.colors.GREEN
            p6.color = ft.colors.GREEN
            misjr
        elif(n == "30"):
            p1.value = "TRES BIEN"
            p1.color = ft.colors.BLUE
            p4.value = "3"
            p4.color = ft.colors.BLUE
            p5.color = ft.colors.BLUE
            p6.color = ft.colors.BLUE
            misjr


    def Fermer(e):
        page.window_destroy()


    btn_fermer = ft.ElevatedButton(text="Fermer", on_click=Fermer)

    cc = ft.Container(
        content=ft.Column(
    [  ft.Row([p1],alignment=ft.MainAxisAlignment.CENTER),
       ft.Row([p2],alignment=ft.MainAxisAlignment.CENTER),
       ft.Row([p3],alignment=ft.MainAxisAlignment.CENTER),
       ft.Row([p4,p5,p6],alignment=ft.MainAxisAlignment.CENTER),
       ft.Row([p7],alignment=ft.MainAxisAlignment.CENTER),
       ft.Row([btn_fermer],alignment=ft.MainAxisAlignment.CENTER,height = 80),
        ]),
        height=300,
        width=600
    )


    c = ft.Container(
    image_src="C:\\Users\\hp\\Desktop\\DRNmem\\views\\rf.png",
    content=cc,
    padding=0,
    margin=0,
    bgcolor=ft.colors.TRANSPARENT, 
    width=740,
    height=490,
    )

    c.alignment = alignment.center


    asyncio.run(aff())

    return ft.View(
        "/resultat_view",
        controls=[c]
    )