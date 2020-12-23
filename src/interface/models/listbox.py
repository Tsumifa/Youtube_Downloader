# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk
    from tkinter import ttk as ttk

except Exception as e:
    raise e

# == LOGIC PART == #


class Listbox:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self, place, elmements):
        self.values = []
        for i in elmements:
            self.values.append(i)
        self.LISTBOX = ttk.Combobox(place, values=self.values, state='readonly',
        font=('Courier', 15, 'bold'), justify='center')
        self.LISTBOX.current(0)
        return self.LISTBOX