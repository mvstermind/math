import flet as ft
from mathgenerator import addition, multiplication, division, subtraction


problem, solution = addition()
problem, solution = problem.replace("$", ""), solution.replace("$", "")


def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "This field cannot be empty"
            page.update()
        else:
            answer = txt_name.value
            page.clean()
            if int(answer) == int(solution):
                page.add(ft.Text("Good job homie"))
            else:
                page.add(ft.Text(f"Almost, answer is {answer}"))

    page.add(ft.Text(f"{problem}"))
    txt_name = ft.TextField(label="Answer")

    page.add(txt_name, ft.ElevatedButton("Submit", on_click=btn_click))


ft.app(target=main)
