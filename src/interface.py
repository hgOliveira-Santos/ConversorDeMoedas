import flet as ft
from componentes import *

def main(page: ft.Page):
    page.title = "Conversor de moedas"
    page.scroll = "adaptative"
    page.window_width = 500
    page.window_height = 600

    page.bgcolor = ft.colors.BLUE_GREY_900

    input_container = ft.Container(
        content=valor_input,
        alignment=ft.alignment.center,
        padding=20,
        bgcolor=ft.colors.BLUE_GREY_900
    )

    page.add(
        input_container
    )

if __name__ == "__main__":
    ft.app(target=main)