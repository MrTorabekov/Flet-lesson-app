import flet as ft
from flet import Row
def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()
    new_task = ft.TextField(hint_text="what's needs to be done?",color='green',width=250)
    page.add(Row([new_task,ft.ElevatedButton('add',on_click=add_clicked)]))

ft.app(target=main)