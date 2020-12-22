# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Root:

    def __init__(self, _settings, _languages, _themes, _menu, _title):
        '''
            initialisation des objets herites de <main>
        '''
        #- controllers
        self.setting = _settings
        self.language = _languages
        self.theme = _themes

        #- models
        self.menu = _menu
        self.title = _title
        '''
            creation de la page + affichage
        '''
        self.initialize_window()
        self.create_widget()
        self.WINDOW.mainloop()

    def initialize_window(self):
        '''
            definition des parametres principaux de la page
        '''
        self.WINDOW = tk.Tk()
        self.WINDOW.geometry(self.setting.get_settings_data("window_size"))
        self.WINDOW.resizable(0, 0)
        self.WINDOW.title(self.language.get_text('title'))
        self.WINDOW.iconbitmap(self.setting.get_settings_data("icon"))
        self.WINDOW.configure(background=self.theme.get_theme("backgroundColor"))


    def create_widget(self):
        '''
            Menu en haut de la page
        '''
        self.MENU = self.menu.create_content()
        self.WINDOW.config(menu=self.MENU)

        '''
            Titre de la page
        '''
        self.TITLE = self.title.create_content('title')
        self.TITLE.pack()

    