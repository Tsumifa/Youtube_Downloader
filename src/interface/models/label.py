# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Title:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self, content):
        self.title = tk.Label(text=self.language.get_text(content),
        background=self.theme.get_theme('backgroundColor'),
        foreground=self.theme.get_theme("textColor"))
        self.title.config(font=("Courier", 44))
        return self.title
