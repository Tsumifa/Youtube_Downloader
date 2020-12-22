# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Root:

    def __init__(self, _settings, _languages, _themes, _menu, _label, _entry, _labelframe):
        '''
            initialisation des objets herites de <main>
        '''
        #- controllers
        self.setting = _settings
        self.language = _languages
        self.theme = _themes

        #- models
        self.menu = _menu
        self.label = _label
        self.labelframe = _labelframe
        self.entry = _entry
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
        self.TITLE = self.label.create_title(self.WINDOW, 'title')
        self.TITLE.pack()

        '''
            Emplacement du conteneur url de la video + saisie url
            
        '''
        self.URL_CONTAINER = self.labelframe.create_content('video')
        self.URL_CONTAINER.pack(pady=30)
        self.URL_PLACEHOLDER = self.label.create_placeholder(self.URL_CONTAINER, 'url')
        self.URL_PLACEHOLDER.pack(pady=5)
        self.URL_ENTRY = self.entry.create_content(self.URL_CONTAINER, 'url')
        self.URL_ENTRY.pack()

        '''
            Emplacement parametrage du telechargement :
                - Saisie nom du fichier
                - emplacement de stockage
                - Saisie type telechargement (mp3 ou mp4)
        '''
        self.SETTING_CONTAINER = self.labelframe.create_content('advanced_settings')
        self.SETTING_CONTAINER.pack(pady=30)
        self.NAME_ENTRY = self.entry.create_content(self.SETTING_CONTAINER, 'name')
        self.NAME_ENTRY.pack()
    