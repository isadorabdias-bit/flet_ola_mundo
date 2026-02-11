import flet as ft 

def main(page: ft.Page):
    page.title = "Meu Primeiro app Flet"
    page.bgcolor = "#f048d1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="renan"),
        ft.ElevatedButton("Clique aqui")
    )

ft.run(main)
