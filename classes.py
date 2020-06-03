import random
import tkinter as tk

widgets_list = []


def do_nothing():
    pass


class List:
    def __init__(self, path):
        self.__path = path
        self.elements = []

    def __str__(self):
        self.get_elements()
        return f'A array of objects.\n File: {self.__path} \n Size: {len(self.elements)}\n Elements:{self.elements}'

    def get_elements(self):
        try:
            with open(self.__path, 'r') as file:
                self.elements = file.read().strip().split('\n')
                if not self.elements[-1]:
                    self.elements.pop()
        except FileNotFoundError:
            self.elements = []

    def save(self):
        with open(self.__path, 'w') as file:
            for element in self.elements:
                file.write(element + '\n')

    def choose_random(self):
        try:
            randomized = random.choice(self.elements)
            return randomized
        except IndexError:
            pass

    def add_element(self, element):
        self.elements.append(element)
        self.save()

    def remove_element(self, index):
        self.elements.pop(index)
        self.save()

    def replace_element(self, index, new):
        self.elements[index] = new
        self.save()

    def show(self):
        lbox = tk.Listbox()
        widgets_list.append(lbox)
        lbox.place(relx=.2, rely=.1, relwidth=.75, relheight=.55)

        scroll = tk.Scrollbar(command=lbox.yview)
        widgets_list.append(scroll)
        scroll.place(relx=.18, rely=.1, relwidth=.02, relheight=.55)
        lbox.config(yscrollcommand=scroll.set)

        for element in self.elements:
            lbox.insert(tk.END, element)

        return lbox


class Button:
    name = 'Button'
    font = 'Arial 24'
    justify = 'center'
    bg = '#ff8521'
    fg = '#ffffff'
    highlightcolor = '#c26417'
    activebackground = '#e66700'
    relx = .25
    rely = .25
    relwidth = .5
    relheight = .125

    def __init__(self, text, command=do_nothing):
        self.__text = text
        self.__command = command
        self.__button = tk.Button(text=self.__text, font=self.font, justify=self.justify,
                                  bg=self.bg, fg=self.fg, highlightcolor=self.highlightcolor,
                                  activebackground=self.activebackground, command=self.__command)

    def __str__(self):
        return 'Button: ' + self.name

    def place_button(self):
        self.__button.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)
        widgets_list.append(self)

    def destroy(self):
        self.__button.place_forget()


class MenuButton(Button):
    name = 'Menu Button'
    font = 'Arial 34'
    bg = '#ff8521'
    fg = '#ffffff'
    highlightcolor = '#c26417'
    activebackground = '#e66700'
    relx = .25
    rely = .1
    relwidth = .5
    relheight = .2


class OptionsButton(Button):
    name = 'Options Button'
    font = 'Arial 20'
    bg = '#ff8521'
    fg = '#ffffff'
    highlightcolor = '#c26417'
    activebackground = '#e66700'
    relx = .1
    rely = .7
    relwidth = .3
    relheight = .2


class InListButton(Button):
    name = 'Delete Button'
    font = 'Arial 17'
    bg = '#ff8521'
    fg = '#ffffff'
    highlightcolor = '#c26417'
    activebackground = '#e66700'
    relx = .02
    rely = .1
    relwidth = .14
    relheight = .07
