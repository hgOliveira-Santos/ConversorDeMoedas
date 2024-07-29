import flet as ft

opções_moedas = [
    "BRL",
    "USD",
    "EUR",
    "GBP",
    "JPY",
]

valor_input = ft.TextField(
    value="Valor a ser convertido",
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

botão_seleção_moeda = ft.Dropdown(
    options=[ft.dropdown.Option(x) for x in opções_moedas],
    width=300,
    value=opções_moedas[0],
    alignment=ft.alignment.center,
    border_color=ft.colors.WHITE
)

botão_conversão = ft.ElevatedButton(
    text="Converter",
    bgcolor=ft.colors.TEAL_400,
    color=ft.colors.BLACK87,
    width=150,
    height=40
)

conversão_bt_container = ft.Container(
    content=botão_conversão,
    padding=0,
    alignment=ft.alignment.center
)

container = ft.Container(
    content=ft.Column(
        controls=[
            valor_input,
            moeda_origem_label,
            botão_seleção_moeda,
            moeda_destino_label,
            botão_seleção_moeda  # Assumindo que você quis adicionar o dropdown de destino aqui
        ]
    ),
    alignment=ft.alignment.center,
    padding=20,
    bgcolor=ft.colors.BLUE_GREY_900
)
