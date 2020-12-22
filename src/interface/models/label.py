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

    def create_content(self, place, content):
        self.title = tk.Label(place, text=self.language.get_text(content),
        background=self.theme.get_theme('backgroundColor'),
        foreground=self.theme.get_theme("textColor"))
        self.title.config(font=("Courier", 44))
        return self.title


class Placeholder:
    
    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self, place, text):
        self.placeholder = tk.Label(place, text=self.language.get_text(text),
        background=self.theme.get_theme('backgroundColor'),
        foreground=self.theme.get_theme("textColor"))
        self.placeholder.config(font=("Courier", 15))
        return self.placeholder


class Create_Label:

    def __init__(self, _language, _theme):
        self.language = _language
        self.theme = _theme
        self.title = Title(self.language, self.theme)
        self.placeholder = Placeholder(self.language, self.theme)

    def create_title(self, place, content):
        return self.title.create_content(place, content)

    def create_placeholder(self, place, text):
        return self.placeholder.create_content(place, text)