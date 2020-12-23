# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Options_Window:

    def __init__(self, _settings, _language, _theme, _combobox, _label, _button, _alert):
        '''
            initialisation des classes heritees de <root>
        '''
        
        self.settings = _settings
        self.language = _language
        self.theme = _theme

        #- models
        self.listbox = _combobox
        self.label = _label
        self.button = _button
        self.alert = _alert

    def change_settings(self):
        self.alert.create_classic_alert('restart')
        self.settings.change_setting('language', self.LANGUAGES_LISTBOX.get())
        self.settings.change_setting('theme', self.THEME_LISTBOX.get())
        print("language : {}, theme : {}".format(self.LANGUAGES_LISTBOX.get(), self.THEME_LISTBOX.get()))
        exit()

    def initialize_window(self, parent):
        self.parent = parent
        '''
            parametres de la fenetre
        '''
        self.WINDOW = tk.Tk()
        self.WINDOW.geometry(self.settings.get_settings_data("option_window_size"))
        self.WINDOW.title(self.language.get_text("settings"))
        self.WINDOW.iconbitmap(self.settings.get_settings_data("icon"))
        self.WINDOW.configure(background=self.theme.get_theme("backgroundColor"))
        self.WINDOW.resizable(0, 0)


        '''
            affichage du contenu de la fenetre
        '''
        self.create_widget()

        '''
            affichage de la fenetre
        '''
        self.WINDOW.mainloop()

    def create_widget(self):

        '''
            Titre de la page
        '''
        self.TITLE = self.label.create_title(self.WINDOW, 'settings')
        self.TITLE.pack(pady=20)

        '''
            Pour choisir le language de l'application
        '''
        self.LANGUAGE_PLACEHOLDER = self.label.create_placeholder(self.WINDOW, 'select_language')
        self.LANGUAGE_PLACEHOLDER.pack(pady=5)
        self.LANGUAGES_LISTBOX = self.listbox.create_content(self.WINDOW, self.settings.get_settings_data('language_list'))
        self.LANGUAGES_LISTBOX.current(self.settings.get_settings_data('language_list').index(self.settings.get_settings_data('language')))
        self.LANGUAGES_LISTBOX.pack(pady=10)

        '''
            Pour choisir le theme de l'application
        '''
        self.THEME_PLACEHOLDER = self.label.create_placeholder(self.WINDOW, 'select_theme')
        self.THEME_PLACEHOLDER.pack(pady=5)
        self.THEME_LISTBOX = self.listbox.create_content(self.WINDOW, self.settings.get_settings_data('theme_list'))
        self.THEME_LISTBOX.current(self.settings.get_settings_data('theme_list').index(self.settings.get_settings_data('theme')))
        self.THEME_LISTBOX.pack(pady=10)

        '''
            Boutton pour valider les choix
        '''
        self.SUBMIT_BUTTON = self.button.create_submit_button(self.WINDOW, 'apply')
        self.SUBMIT_BUTTON.configure(width=30, command=self.change_settings)
        self.SUBMIT_BUTTON.pack(pady=20, side='bottom')
