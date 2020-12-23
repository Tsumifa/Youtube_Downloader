# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Browse_Button:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self, place, text):
        self.button = tk.Button(place, text=self.language.get_text(text), relief='groove',
        font=('Courier', 12, 'bold'), background=self.theme.get_theme('entryBackgroundColor'),
        foreground=self.theme.get_theme("textColor"))
        return self.button


class Submit_Button:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self, place, text):
        self.button = tk.Button(place, text=self.language.get_text(text), relief='raised',
        font=('Courier', 15, 'bold'), background=self.theme.get_theme('validate'),
        foreground=self.theme.get_theme("textColor"), width=75)
        return self.button


class Button:
    
    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme
        
        '''
            initialisation des sous classes Bouton
        '''
        self.browse_button = Browse_Button(self.language, self.theme)
        self.submit_button = Submit_Button(self.language, self.theme)

    def create_browse_button(self, place, text):
        return self.browse_button.create_content(place, text)

    def create_submit_button(self, place, text):
        return self.submit_button.create_content(place, text)