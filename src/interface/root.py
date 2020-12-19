
# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

    #- Files

    # Controllers
    import controllers.settings as settings
    import controllers.language as languages
    import controllers.theme as themes

    # Models
    import models.menu as menu

except Exception as e:
    raise e
# == LOGIC PART == #


class Root:

    def __init__(self):
        
        '''
            initialisation des classes type controlleur pour afficher le contenu adapter
        '''
        self.setting = settings.Settings()
        self.theme = themes.Theme(self.setting.get_settings_data("theme"))
        self.language = languages.Language(self.setting.get_settings_data("language"))

        '''
            Creation de la fenetre principale
        '''

        self.WINDOW = tk.Tk()

        self.create_initial_window()

    # Initial window of the APP
    def create_initial_window(self):
        
        '''
            Configuration fenetre initiale
        '''
        self.WINDOW.geometry(self.setting.get_settings_data('window_size'))
        self.WINDOW.title(self.language.get_text('title'))
        self.WINDOW.iconbitmap(self.setting.get_settings_data('icon'))
        self.WINDOW.configure(background=self.theme.get_theme('backgroundColor'))

        '''
            Widgets fenetre initiale
        '''

        self._menu_frame = tk.Frame(self.WINDOW)
        self._menu_frame.grid()
        '''self.option_name = str(self.language.get_text('settings'))
        self._help_name = str(self.language.get_text('help'))'''

        self.WINDOW.config(menu=menu.Menu(self._menu_frame))
        self.WINDOW.mainloop()
        pass

root = Root()
print(root.theme.get_theme("backgroundColor"))
print(root.language.get_text("title"))
