# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk
    from tkinter.messagebox import *

except Exception as e:
    raise e

# == LOGIC PART == #


class Classic_Alert:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self, text):
        return showwarning(self.language.get_text('warning'), self.language.get_text(text))


class Alert:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

        '''
            Initialisation des differentes alertes
        '''
        self.classic_alert = Classic_Alert(self.language, self.theme)

    def create_classic_alert(self, text):
        return self.classic_alert.create_content(text)