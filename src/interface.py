import flet as ft
from conversão_moedas import converter_moeda
from decimal import Decimal

opções_moedas = [
    "BRL",
    "USD",
    "EUR",
    "BTC"
]

def conversão(valor, moeda_origem, moeda_destino, resultado_label, page):
    try:
        cot = converter_moeda(moeda_origem, moeda_destino)
        resultado = float(valor) * float(cot)
        print(resultado)
        resultado_label.value = f"Resultado: {Decimal(str(resultado)):.2f} {moeda_destino}"
    except ValueError:
        resultado_label.value = "Valor inválido!"
    except Exception as e:
        resultado_label.value = f"Erro: {str(e)}"
    
    resultado_label.visible = True
    page.update()

def main(page: ft.Page):
    page.title = "Conversor de moedas"
    page.scroll = "adaptive"
    page.window_width = 500
    page.window_height = 600

    page.bgcolor = ft.colors.BLUE_GREY_900

    valor_input = ft.TextField(
        hint_text="Valor a ser convertido",
        cursor_color=ft.colors.WHITE,
        width=300,
        border_color=ft.colors.WHITE
    )

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

    seleção_moeda_origem_bt = ft.Dropdown(
        options=[ft.dropdown.Option(x) for x in opções_moedas],
        width=300,
        value=opções_moedas[0],
        alignment=ft.alignment.center,
        border_color=ft.colors.WHITE
    )

    seleção_moeda_destino_bt = ft.Dropdown(
        options=[ft.dropdown.Option(x) for x in opções_moedas],
        width=300,
        value=opções_moedas[0],
        alignment=ft.alignment.center,
        border_color=ft.colors.WHITE
    )

    input_container = ft.Container(
        content=ft.Column(
            controls=[valor_input]
        ),
        alignment=ft.alignment.center,
        padding=10,
        bgcolor=ft.colors.BLUE_GREY_900
    )

    moeda_origem_container = ft.Container(
        content=ft.Column(
            controls=[moeda_origem_label, seleção_moeda_origem_bt]
        ),
        alignment=ft.alignment.center,
        padding=10,
        bgcolor=ft.colors.BLUE_GREY_900
    )

    moeda_destino_container = ft.Container(
        content=ft.Column(
            controls=[moeda_destino_label, seleção_moeda_destino_bt]
        ),
        alignment=ft.alignment.center,
        padding=10,
        bgcolor=ft.colors.BLUE_GREY_900
    )

    resultado_label = ft.Text(
        value="",
        font_family="JetBrains mono",
        size=16,
        color=ft.colors.WHITE,
        visible=False
    )

    botão_conversão = ft.ElevatedButton(
        text="Converter",
        bgcolor=ft.colors.TEAL_400,
        color=ft.colors.BLACK87,
        width=150,
        height=40,
        on_click=lambda e: conversão(
            valor_input.value, 
            seleção_moeda_origem_bt.value, 
            seleção_moeda_destino_bt.value,
            resultado_label,
            page
        )
    )

    conversão_bt_container = ft.Container(
        content=botão_conversão,
        padding=10,
        alignment=ft.alignment.center
    )

    resultado_container = ft.Container(
        content=resultado_label,
        padding=20,
        alignment=ft.alignment.center
    )

    page.add(
        input_container,
        moeda_origem_container,
        moeda_destino_container,
        conversão_bt_container,
        resultado_container
    )

if __name__ == "__main__":
    ft.app(target=main)
