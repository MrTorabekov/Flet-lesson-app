import flet as ft
from flet import Column,Text

def main(page: ft.Page):
    page.add(Column(
        controls=[
            Text('Hello'),
            Text('Hi')
        ]
    ))

ft.app(main)