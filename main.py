import os
import random
import tkinter as tk
# from tkinter import messagebox as mb
import strings as st
from classes import MenuButton, OptionsButton, widgets, strings

root = tk.Tk()

if not os.path.exists('data\\'):
    os.mkdir('data\\')


def get_list_from_file(file_path):
    with open(file_path, 'r') as file:
        try:
            lis = file.read().strip().split('\n')
            if len(lis) > 1:
                if not lis[-1]:
                    players.pop()
        except FileNotFoundError():
            lis = []

    return lis


def save():
    for file_path in ['data\\questions.txt', 'data\\tasks.txt', 'data\\players.txt']:
        for lis in [questions, tasks, players]:
            with open(file_path, 'w') as file:
                for element in lis:
                    file.write(element + '\n')


def choose_random(lis):
    try:
        randomized = random.choice(lis)
        return randomized
    except IndexError:
        pass


def show(lis):
    clear()
    lbox = tk.Listbox()
    widgets.append(lbox)
    lbox.place(relx=.2, rely=.1, relwidth=.75, relheight=.55)

    scroll = tk.Scrollbar(command=lbox.yview)
    widgets.append(scroll)
    scroll.place(relx=.18, rely=.1, relwidth=.02, relheight=.55)
    lbox.config(yscrollcommand=scroll.set)

    for element in lis:
        lbox.insert(tk.END, element)

    obj = ''
    if lis == players:
        obj = st.player.text
    if lis == questions:
        obj = st.question.text
    if lis == tasks:
        obj = st.task.text

    add_btn = OptionsButton(st.add.text + '\n' + obj, lambda: add(lis))
    add_btn.relx = .7
    add_btn.place_button()

    menu_btn = OptionsButton(st.main_menu.text, main_menu)
    menu_btn.relx = .05
    menu_btn.place_button()


def add(lis):
    main_menu()


questions = get_list_from_file('data\\questions.txt')
tasks = get_list_from_file('data\\tasks.txt')
players = get_list_from_file('data\\players.txt')


def main_menu():
    clear()

    play_btn = MenuButton(st.play.text, play)
    play_btn.place_button()

    settings_btn = MenuButton(st.settings.text, settings)
    settings_btn.rely = .4
    settings_btn.place_button()

    exit_btn = MenuButton(st.exit_.text, exit)
    exit_btn.rely = .7
    exit_btn.place_button()


def play():
    show(players)

    start_btn = OptionsButton(st.start.text, start)
    start_btn.relx = .375
    start_btn.place_button()


def start():
    clear()

    player = choose_random(players)
    label = tk.Label(text=f'{player}, {st.truth_dare.text}', font='Arial 30')
    widgets.append(label)
    label.place(relx=.1, rely=.1, relwidth=.8)

    truth_btn = OptionsButton(st.truth.text, lambda: truth_or_dare(player, questions))
    truth_btn.place_button()

    dare_btn = OptionsButton(st.dare.text, lambda: truth_or_dare(player, tasks))
    dare_btn.relx = .6
    dare_btn.place_button()


def truth_or_dare(player, lis):
    clear()

    choice = choose_random(lis)
    text = f'{player}, {choice}'
    text = f'{text[0:35]}\n{text[35:70]}\n{text[70:105]}\n{text[105:140]}\n{text[140:175]}\n{text[175:210]}'
    label = tk.Label(text=text, font='Arial 30')
    widgets.append(label)
    label.place(relx=.1, rely=.1, relwidth=.8)

    menu_btn = OptionsButton(st.main_menu.text, main_menu)
    menu_btn.place_button()

    continue_btn = OptionsButton(st.continue_.text, start)
    continue_btn.relx = .6
    continue_btn.place_button()


def settings():
    clear()

    lan_btn = OptionsButton(st.lang.text, lang)
    lan_btn.rely = .1
    lan_btn.place_button()

    rules_btn = OptionsButton(st.rules.text, rules)
    rules_btn.relx = .6
    rules_btn.rely = .1
    rules_btn.place_button()

    questions_btn = OptionsButton(st.questions.text, lambda: show(questions))
    questions_btn.rely = .4
    questions_btn.place_button()

    tasks_btn = OptionsButton(st.tasks.text, lambda: show(tasks))
    tasks_btn.relx = .6
    tasks_btn.rely = .4
    tasks_btn.place_button()

    menu_btn = OptionsButton(st.main_menu.text, main_menu)
    menu_btn.relx = .3
    menu_btn.relwidth = .4
    menu_btn.place_button()


def clear():
    for widget in widgets:
        try:
            widget.destroy()
        except TypeError:
            widget.pack_forget()

    widgets.clear()


def lang():
    clear()

    eng_btn = MenuButton('ENGLISH', lambda: set_lang('eng'))
    eng_btn.place_button()

    rus_btn = MenuButton('РУССКИЙ', lambda: set_lang('rus'))
    rus_btn.rely = .4
    rus_btn.place_button()

    back_btn = MenuButton(st.back.text, settings)
    back_btn.rely = .7
    back_btn.place_button()


def set_lang(language):
    for string in strings:
        string.set_lang(language)
    root.title(st.title.text)

    clear()
    lang()


def rules():
    pass


root.geometry('900x500')
root.minsize(675, 375)

set_lang('eng')
main_menu()

root.mainloop()
