import os
import tkinter as tk
from tkinter import messagebox as mb
import strings as st
from classes import MenuButton, OptionsButton, InListButton, List, widgets, strings

root = tk.Tk()
file_path = 'data\\'

if not os.path.exists(file_path):
    os.mkdir(file_path)

players = List(file_path + 'players.txt')
questions = List(file_path + 'questions.txt')
tasks = List(file_path + 'tasks.txt')

players.get_elements()
questions.get_elements()
tasks.get_elements()


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


def play(list_class=players):
    show(list_class)

    start_btn = OptionsButton(st.start.text, start)
    start_btn.relx = .35
    start_btn.place_button()


def start():
    clear()

    player = players.choose_random()
    label = tk.Label(text=f'{player}, {st.truth_dare.text}', font='Arial 30')
    widgets.append(label)
    label.place(relx=.1, rely=.1, relwidth=.8)

    truth_btn = OptionsButton(st.truth.text, lambda: truth_or_dare(player, questions))
    truth_btn.place_button()

    dare_btn = OptionsButton(st.dare.text, lambda: truth_or_dare(player, tasks))
    dare_btn.relx = .6
    dare_btn.place_button()


def truth_or_dare(player, list_class):
    clear()

    random = list_class.choose_random()
    text = f'{player}, {random}'
    text = f'{text[0:35]}\n{text[35:70]}\n{text[70:105]}\n{text[105:140]}\n{text[140:175]}\n{text[175:210]}'
    label = tk.Label(text=text, font='Arial 30')
    widgets.append(label)
    label.place(relx=.1, rely=.1, relwidth=.8)

    menu_btn = OptionsButton(st.main_menu.text, main_menu)
    menu_btn.place_button()

    continue_btn = OptionsButton(st.continue_.text, start)
    continue_btn.relx = .6
    continue_btn.place_button()


def show(list_class):
    clear()
    lbox = list_class.show()

    func = play if list_class == players else show
    entry = tk.Entry(font='Arial 25') if list_class == players else tk.Text(font='Arial 25')
    relheight = .1 if list_class == players else .3
    word = string = ''

    if list_class == players:
        word = st.player
        string = st.enter_player.text

    if list_class == questions:
        word = st.question
        string = st.enter_question.text

    if list_class == tasks:
        word = st.task
        string = st.enter_task.text

    def add(replace=False):
        element = ''
        if replace:
            select = lbox.curselection()

            if select != ():
                index = lbox.index(select)
                element = list_class.elements[index]
            else:
                replace = False

        clear()

        label = tk.Label(text=string, font='Arial 30')
        widgets.append(label)
        label.place(relx=.1, rely=.1, relwidth=.8)

        widgets.append(entry)
        entry.place(relx=.2, rely=.25, relwidth=.6, relheight=relheight)
        if list_class == players:
            entry_index = 0
        else:
            entry_index = 1.0
        entry.insert(entry_index, element)

        def confirm():
            if replace:
                if list_class == players:
                    players.replace_element(index, entry.get())
                else:
                    list_class.replace_element(index, entry.get(1.0, tk.END))
                func(list_class)
            else:
                if list_class == players:
                    players.add_element(entry.get())
                else:
                    list_class.add_element(entry.get(1.0, tk.END))
                func(list_class)

        cancel_btn = OptionsButton(st.cancel.text, lambda: func(list_class))
        cancel_btn.place_button()

        confirm_btn = OptionsButton(st.confirm.text, confirm)
        confirm_btn.relx = .6
        confirm_btn.place_button()

    def delete():

        select = lbox.curselection()

        if select != ():
            index = lbox.index(select)
            element = list_class.elements[index]
            answer = mb.askyesno(title=f'{st.delete.text} {word.text}', message=f'{st.del_confirm.text}\n{word.text}: '
                                                                                f'{element}?')
            if answer:
                list_class.remove_element(index)
                lbox.delete(select)

    back_btn = OptionsButton(st.back.text, settings)
    back_btn.relx = .05
    back_btn.relwidth = .25
    back_btn.place_button()

    add_btn = OptionsButton(f'{st.add.text}\n{word.text}', add)
    add_btn.relx = .7
    add_btn.relwidth = .25
    add_btn.place_button()

    edit_btn = InListButton(st.edit.text, lambda: add(True))
    edit_btn.place_button()

    del_btn = InListButton(st.delete.text, delete)
    del_btn.rely = .2
    del_btn.place_button()


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

    rus_btn = MenuButton('Русский', lambda: set_lang('rus'))
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
