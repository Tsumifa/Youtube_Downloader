# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class About_Window:

    def __init__(self, _settings, _language, _theme, _label):
        '''
            initialisation des classes heritees de <root>
        '''
        
        self.settings = _settings
        self.language = _language
        self.theme = _theme

        #- models
        self.label = _label

    def initialize_window(self):
        '''
            Parametre de la fenetre
        '''
        self.WINDOW = tk.Tk()
        self.WINDOW.geometry(self.settings.get_settings_data("alert_window_size"))
        self.WINDOW.title(self.language.get_text("about"))
        self.WINDOW.iconbitmap(self.settings.get_settings_data("icon"))
        self.WINDOW.configure(background=self.theme.get_theme("backgroundColor"))
        self.WINDOW.resizable(0, 0)

        '''
            Affiche les widgets
        '''
        self.create_content()

        '''
            Affiche la fenetre
        '''
        self.WINDOW.mainloop()

    def create_content(self, ):
        self.LABEL = self.label.create_placeholder(self.WINDOW, 'creator')
        self.LABEL.pack(pady=20)