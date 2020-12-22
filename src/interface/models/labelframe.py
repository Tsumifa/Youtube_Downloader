# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Labelframe:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self, name):

        self.labelframe = tk.LabelFrame(text=self.language.get_text(name),
        padx=20, pady=20, background=self.theme.get_theme("frameBackgroundColor"),
        foreground=self.theme.get_theme("textColor"), font=('Courier', 12))
        return self.labelframe