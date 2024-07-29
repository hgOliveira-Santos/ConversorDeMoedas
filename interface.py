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
    page.title = "Conversor de moedas"
    page.scroll = "adaptative"
    page.window_width = 600
    page.window_height = 600

    valor_input = ft.TextField(label="Valor a ser convertido")

    moeda_origem_label = ft.Text(
                            value="Selecione a moeda de origem", 
                            font_family="JetBrains mono", 
                            size=16, 
                            color=ft.colors.WHITE
                        )
    
    moeda_destino_label = ft.Text(
                            value="Selecione a moeda de destino", 
                            font_family="JetBrains mono", 
                            size=16, 
                            color=ft.colors.WHITE
                        )

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
                moeda_origem_label,
                botão_seleção_moeda,
                moeda_destino_label,
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