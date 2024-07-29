import flet as ft

# Lista de opções de moedas
opções_moedas = [
    "BRL",
    "USD",
    "EUR",
    "GBP",
    "JPY",
]

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 600

    valor_input = ft.TextField(label="Valor")

    botão_seleção_moeda = ft.Dropdown(
        options=[ft.dropdown.Option(x) for x in opções_moedas],
        width=300,
        value=opções_moedas[0], 
        alignment=ft.alignment.center
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                valor_input,
                botão_seleção_moeda
            ]
        ),
        alignment=ft.alignment.center,
        padding=20,
        bgcolor=ft.colors.BLUE
    )


    page.add(
        container
    )

if __name__ == "__main__":
    ft.app(target=main)