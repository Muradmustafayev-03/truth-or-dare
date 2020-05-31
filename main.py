import os
import tkinter as tk
from classes import MenuButton, OptionsButton, List, widgets_list

file_path = 'data\\'


def main_menu():
    clear()

    play_btn = MenuButton('PLAY', play)
    play_btn.place_button()

    settings_btn = MenuButton('SETTINGS', settings)
    settings_btn.rely = .4
    settings_btn.place_button()

    exit_btn = MenuButton('EXIT', exit)
    exit_btn.rely = .7
    exit_btn.place_button()


def play():
    show(players)

    start_btn = OptionsButton('START', start)
    start_btn.relx = .35
    start_btn.place_button()


def start():
    clear()

    player = players.choose_random()
    label = tk.Label(text=f'{player}, truth or dare?', font='Arial 30')
    widgets_list.append(label)
    label.place(relx=.1, rely=.1, relwidth=.8)

    truth_btn = OptionsButton('TRUTH', lambda: truth_or_dare(player, questions))
    truth_btn.place_button()

    dare_btn = OptionsButton('DARE', lambda: truth_or_dare(player, tasks))
    dare_btn.relx = .6
    dare_btn.place_button()


def truth_or_dare(player, list_class):
    clear()

    random = list_class.choose_random()
    text = f'{player}, {random}'
    text = f'{text[0:35]}\n{text[35:70]}\n{text[70:105]}\n{text[105:140]}\n{text[140:175]}\n{text[175:210]}'
    label = tk.Label(text=text, font='Arial 30')
    widgets_list.append(label)
    label.place(relx=.1, rely=.1, relwidth=.8)

    main_menu_btn = OptionsButton('MAIN MENU', main_menu)
    main_menu_btn.place_button()

    continue_btn = OptionsButton('CONTINUE', start)
    continue_btn.relx = .6
    continue_btn.place_button()


def show(list_class):
    clear()
    list_class.show()

    if list_class == players:
        word = 'PLAYER'
    elif list_class == questions:
        word = 'QUESTION'
    elif list_class == tasks:
        word = 'TASK'
    else:
        word = None

    main_menu_btn = OptionsButton('MAIN MENU', main_menu)
    main_menu_btn.relx = .05
    main_menu_btn.relwidth = .25
    main_menu_btn.place_button()

    add_btn = OptionsButton(f'ADD NEW\n{word}', lambda: add(list_class))
    add_btn.relx = .7
    add_btn.relwidth = .25
    add_btn.place_button()


def add(list_class):
    clear()

    if list_class == players:
        string = 'name of player'
        func = play
        entry = tk.Entry(font='Arial 25')
        relheight = .1
    elif list_class == questions:
        string = 'text of question'
        func = lambda: show(questions)
        entry = tk.Text(font='Arial 25')
        relheight = .3
    elif list_class == tasks:
        string = 'text of task'
        func = lambda: show(tasks)
        entry = tk.Text(font='Arial 25')
        relheight = .3
    else:
        string = func = entry = relheight = None

    label = tk.Label(text=f'Enter the {string}:', font='Arial 30')
    widgets_list.append(label)
    label.place(relx=.1, rely=.1, relwidth=.8)

    widgets_list.append(entry)
    entry.place(relx=.2, rely=.25, relwidth=.6, relheight=relheight)

    def confirm():
        if list_class == players:
            players.add_element(entry.get())
        else:
            list_class.add_element(entry.get(1.0, tk.END))
        func()

    cancel_btn = OptionsButton('CANCEL', func)
    cancel_btn.place_button()

    confirm_btn = OptionsButton('CONFIRM', confirm)
    confirm_btn.relx = .6
    confirm_btn.place_button()


def settings():
    clear()

    lan_btn = OptionsButton('LANGUAGE')
    lan_btn.rely = .1
    lan_btn.place_button()

    rules_btn = OptionsButton('RULES')
    rules_btn.relx = .6
    rules_btn.rely = .1
    rules_btn.place_button()

    questions_btn = OptionsButton('QUESTIONS', lambda: show(questions))
    questions_btn.rely = .4
    questions_btn.place_button()

    tasks_btn = OptionsButton('TASKS', lambda: show(tasks))
    tasks_btn.relx = .6
    tasks_btn.rely = .4
    tasks_btn.place_button()

    main_menu_btn = OptionsButton('MAIN MENU', main_menu)
    main_menu_btn.relx = .3
    main_menu_btn.relwidth = .4
    main_menu_btn.place_button()


def clear():
    for widget in widgets_list:
        try:
            widget.destroy()
        except TypeError:
            widget.pack_forget()

    widgets_list.clear()


root = tk.Tk()
root.geometry('900x500')
root.minsize(675, 375)
root.title('TRUTH OR DARE')

if not os.path.exists(file_path):
    os.mkdir(file_path)

players = List(file_path + 'players.txt')
questions = List(file_path + 'questions.txt')
tasks = List(file_path + 'tasks.txt')

players.get_elements()
questions.get_elements()
tasks.get_elements()

main_menu()

root.mainloop()
