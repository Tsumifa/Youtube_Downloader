# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Menu:

    def __init__(self, _language, _theme, _options_window, _about_page):
        '''
            initialisation des objets herites de <root>
        '''
        self.language = _language
        self.theme = _theme

        #- views
        self.options_window = _options_window
        self.about_window = _about_page

    def stop_program(self):
        '''
            ferme la fenetre et arrete le programme
        '''
        self.place.quit()

    def show_options_window(self):
        '''
            affiche la page des options
        '''
        self.options_window.initialize_window(self.place)

    def show_about_page(self):
        self.about_window.initialize_window()

    def create_content(self, place):
        self.place = place
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
        self.menu1.add_command(label=self.language.get_text("options"), command=self.show_options_window)
        self.menu_bar.add_cascade(label=self.language.get_text("settings"), menu=self.menu1)

        self.menu2.add_command(label=self.language.get_text('about'), command=self.show_about_page)
        self.menu2.add_command(label=self.language.get_text('documentation'), command=print(''))
        self.menu_bar.add_cascade(label=self.language.get_text('help'), menu=self.menu2)

        self.menu3.add_separator()
        self.menu3.add_command(label=self.language.get_text("quit"), command=self.stop_program)
        self.menu_bar.add_cascade(label=self.language.get_text('quit'), menu=self.menu3)

        return self.menu_bar