import flet as ft
from mathgenerator import addition, division, multiplication, subtraction
import time

streak: int = 0
file_name: str = "data.txt"


def main(page):
    page.title = "Matma"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    get_choice(page)


def get_choice(page):
    def on_choice(e):
        choice_map = {
            "Dzielenie": "division",
            "Mnozenie": "multiplication",
            "Dodawanie": "addition",
            "Odejmowanie": "subtraction",
        }
        choice = choice_map.get(e.control.text, "").lower()
        page.clean()
        choice_handler(page, choice)

    choice_buttons = [
        ft.ElevatedButton(
            text="Dzielenie",
            on_click=on_choice,
            style=ft.ButtonStyle(padding=20),
        ),
        ft.ElevatedButton(
            text="Mnozenie",
            on_click=on_choice,
            style=ft.ButtonStyle(padding=20),
        ),
        ft.ElevatedButton(
            text="Dodawanie",
            on_click=on_choice,
            style=ft.ButtonStyle(padding=20),
        ),
        ft.ElevatedButton(
            text="Odejmowanie",
            on_click=on_choice,
            style=ft.ButtonStyle(padding=20),
        ),
    ]

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Wybierz swojego wojownika",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Row(
                    choice_buttons, alignment=ft.MainAxisAlignment.CENTER, spacing=20
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )


def gen_problem(page, problem_type):
    global streak, problem, solution
    problem, solution = problem_type()
    problem = problem.replace("$", "")
    solution = solution.replace("$", "")

    problem = problem.replace("\\div", "÷").replace("\\cdot", "×")

    def btn_click(e):
        global streak, problem, solution
        if not txt_name.value:
            txt_name.error_text = "Ej no to nie moze byc puste co"
            txt_name.update()
            return False
        else:
            answer = txt_name.value
            if int(answer) == int(solution):
                streak += 1
                with open(file_name, "a") as file:
                    file.write(str(streak) + "\n")
                page.clean()
                gen_problem(page, problem_type)
                return True
            else:
                page.clean()
                page.add(
                    ft.Text(
                        f"Zle, odpowiedz to: {solution}",
                        size=25,
                        color=ft.colors.RED,
                    )
                )
                time.sleep(2)
                page.clean()
                gen_problem(page, problem_type)
                return True

    def back_to_menu(e):
        page.clean()
        get_choice(page)

    button = ft.ElevatedButton(
        "Menu",
        on_click=back_to_menu,
    )
    page.add(button)
    page.add(
        ft.Column(
            [
                ft.Text(f"{problem}", size=30, text_align=ft.TextAlign.CENTER),
                txt_name := ft.TextField(label="Odpowiedz", width=200, text_size=20),
                ft.ElevatedButton(
                    "Dalej",
                    on_click=btn_click,
                    style=ft.ButtonStyle(padding=20),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )

    page.add(
        ft.Text(
            f"Poprawne odpowiedzi: {streak}",
            text_align=ft.TextAlign.CENTER,
            size=20,
            color=ft.colors.GREEN_100,
        ),
        ft.Text(
            f"Wszystkie odpowiedzi: {read_streak(file_name)}",
            text_align=ft.TextAlign.CENTER,
            size=20,
            color=ft.colors.GREEN_500,
        ),
    )


def choice_handler(page, choice):
    match choice:
        case "division":
            gen_problem(page, division)
        case "multiplication":
            gen_problem(page, multiplication)
        case "addition":
            gen_problem(page, addition)
        case "subtraction":
            gen_problem(page, subtraction)


def read_streak(file: str) -> str:
    try:
        with open(file, "r") as content:
            lines = content.readlines()
            total_streaks = len(lines)
        return str(total_streaks)
    except FileNotFoundError:
        return "0"


ft.app(target=main)
