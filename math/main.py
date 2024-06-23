import flet as ft

import mathgenerator


def main(page):
    problem, solution = mathgenerator.addition()
    solution = int(solution)

    problem = problem.replace("$", "")

    def button_click(e):
        if answer == solution:
            page.add(ft.Text(value="brawo"))

    t = ft.Text(value=problem)
    page.add(t)
    answer = ft.TextField(hint_text="Answer")
    page.add(answer, ft.ElevatedButton("Say hello!", on_click=button_click))


ft.app(target=main)
