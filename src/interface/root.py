# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Root:

    def __init__(self, window_size, window_title, window_background, window_icon_path):
        
        '''
            Create window
        '''
        self.WINDOW = tk.Tk()

        '''
            Settings of the window
        '''
        self.GEOMETRY = window_size
        self.TITLE = window_title
        self.BACKGROUND = window_background
        self.ICON = window_icon_path


    def initialize_window(self):
        self.WINDOW.title(self.TITLE)
        self.WINDOW.geometry(self.GEOMETRY)
        self.WINDOW.iconbitmap(self.ICON)
        self.WINDOW.configure(background=self.BACKGROUND)

    def create_widget(self):
        pass