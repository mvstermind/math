import flet as ft
from mathgenerator import addition, division, multiplication, subtraction
import time

streak = 0


def main(page):
    get_choice(page)


def get_choice(page):
    def on_choice(e):
        choice = e.control.text.lower()
        page.clean()
        choice_handler(page, choice)

    page.add(ft.Text("Choose your subject"))
    page.add(ft.ElevatedButton(text="Division", on_click=on_choice))
    page.add(ft.ElevatedButton(text="Multiplication", on_click=on_choice))
    page.add(ft.ElevatedButton(text="Addition", on_click=on_choice))
    page.add(ft.ElevatedButton(text="Subtraction", on_click=on_choice))


def gen_problem(page, problem_type):
    global streak, problem, solution
    problem, solution = problem_type()
    problem, solution = problem.replace("$", ""), solution.replace("$", "")

    def btn_click(e):
        global streak, problem, solution
        if not txt_name.value:
            txt_name.error_text = "This field cannot be empty"
            txt_name.update()
            return False
        else:
            answer = txt_name.value
            if int(answer) == int(solution):
                streak += 1
                page.clean()
                page.add(ft.Text(f"Good job homie, {streak} answers "))
                time.sleep(2)
                page.clean()
                gen_problem(page, problem_type)
                return True
            else:
                page.clean()
                page.add(ft.Text(f"Almost, answer is {solution}"))
                time.sleep(2)
                page.clean()
                gen_problem(page, problem_type)
                return True

    page.add(ft.Text(f"{problem}"))
    txt_name = ft.TextField(label="Answer")

    page.add(txt_name, ft.ElevatedButton("Submit", on_click=btn_click))


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


ft.app(target=main)
