# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Menu:

    def __init__(self, _language, _theme):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

    def create_content(self):
        '''
            creation du conteneur menu 
        '''
        self.menu_bar = tk.Menu()

        '''
            creation des composants du menu
        '''
        #- Les composants directs (affiches constament)
        self.menu1 = tk.Menu(self.menu_bar, tearoff=0)
        self.menu2 = tk.Menu(self.menu_bar, tearoff=0)
        self.menu3 = tk.Menu(self.menu_bar, tearoff=0)
        
        #- Les composants indirects (affiches lorsque clique)
        self.menu1.add_command(label=self.language.get_text("options"), command=print("quitté"))
        self.menu_bar.add_cascade(label=self.language.get_text("settings"), menu=self.menu1)

        self.menu2.add_command(label=self.language.get_text('about'), command=print('couper'))
        self.menu2.add_command(label=self.language.get_text('documentation'), command=print('copier'))
        self.menu_bar.add_cascade(label=self.language.get_text('help'), menu=self.menu2)

        self.menu3.add_separator()
        self.menu3.add_command(label=self.language.get_text("quit"), command=print('a propos'))
        self.menu_bar.add_cascade(label=self.language.get_text('quit'), menu=self.menu3)

        return self.menu_bar