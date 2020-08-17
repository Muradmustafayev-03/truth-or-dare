import tkinter as tk

widgets = []
strings = []


class String:
    def __init__(self, eng, rus):
        strings.append(self)
        self.eng = eng
        self.rus = rus
        self.text = ''

    def set_lang(self, lang):
        if lang == 'eng':
            self.text = self.eng
        elif lang == 'rus':
            self.text = self.rus


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

    def __init__(self, text, command):
        self.__text = text
        self.__command = command
        self.__button = tk.Button(text=self.__text, font=self.font, justify=self.justify,
                                  bg=self.bg, fg=self.fg, highlightcolor=self.highlightcolor,
                                  activebackground=self.activebackground, command=self.__command)

    def __str__(self):
        return 'Button: ' + self.name

    def place_button(self):
        self.__button.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)
        widgets.append(self)

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
    relwidth = .25
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
