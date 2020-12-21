# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Button:

    def __init__(self, language_data, theme_data):
        self.language = language_data
        self.theme = theme_data
        self.create_button()

    def create_button(self):
        self.button = tk.Button()
