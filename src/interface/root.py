# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk
    from tkinter import filedialog as _filedialog

except Exception as e:
    raise e

# == LOGIC PART == #


class Root:

    def __init__(self, _settings, _languages, _themes, _menu, _label, _entry, _labelframe, _listbox, _button, _options_window, _alert, _downloader):
        '''
            initialisation des objets herites de <main>
        '''
        #- controllers
        self.setting = _settings
        self.language = _languages
        self.theme = _themes

        #- models
        self.menu = _menu
        self.label = _label
        self.labelframe = _labelframe
        self.entry = _entry
        self.listbox = _listbox
        self.button = _button
        self.alert = _alert

        #- views
        self.options_window = _options_window

        #- Backend
        self.folder_path = 'C:/Users/Thomas/Downloads'
        self.downloader = _downloader

        '''
            creation de la page + affichage
        '''
        self.initialize_window()
        self.create_widget()
        self.WINDOW.mainloop()

    def check_inputs(self):
        '''
            verifie si les champs d'entree sont correctement remplis
        '''
        if self.URL_ENTRY.get() == '':
            self.URL_ALERT = self.alert.create_classic_alert('url_unfilled')
            return 1


    def dowload_video(self):
        
        if self.check_inputs() != 1:
            print(self.FORMAT_LISTBOX.get())
            errors = self.downloader.download(self.URL_ENTRY.get(), self.LISTBOX.get(), self.NAME_ENTRY.get(), self.folder_path, self.FORMAT_LISTBOX.get())
            if errors == 1:
                self.ALERT_DOWNLOAD = self.alert.create_classic_alert('something_went_wrong')
            elif errors == 2:
                self.ALERT_DOWNLOAD = self.alert.create_classic_alert('video_not_free')
            elif errors == 0:
                self.ALERT_DOWNLOAD = self.alert.create_classic_alert('video_downloaded')
        else:
            self.ALERT_DOWNLOAD = self.alert.create_classic_alert('something_went_wrong')

    def browse_forlder(self):
        self.folder_path = _filedialog.askdirectory()
        self.LABEL_PATH = self.label.create_path_label(self.SETTING_CONTAINER, self.folder_path)
        self.LABEL_PATH.grid(pady=10, row=2, column=1, columnspan=2)

    def initialize_window(self):
        '''
            definition des parametres principaux de la page
        '''
        self.WINDOW = tk.Tk()
        self.WINDOW.geometry(self.setting.get_settings_data("window_size"))
        self.WINDOW.resizable(0, 0)
        self.WINDOW.title(self.language.get_text('title'))
        self.WINDOW.iconbitmap(self.setting.get_settings_data("icon"))
        self.WINDOW.configure(background=self.theme.get_theme("backgroundColor"))


    def create_widget(self):
        '''
            Menu en haut de la page
        '''
        self.MENU = self.menu.create_content(self.WINDOW)
        self.WINDOW.config(menu=self.MENU)

        '''
            Titre de la page
        '''
        self.TITLE = self.label.create_title(self.WINDOW, 'title')
        self.TITLE.pack(pady=20)

        '''
            Emplacement du conteneur url de la video + saisie url
            
        '''
        self.URL_CONTAINER = self.labelframe.create_content('video')
        self.URL_CONTAINER.pack(pady=30)
        self.URL_PLACEHOLDER = self.label.create_placeholder(self.URL_CONTAINER, 'url')
        self.URL_PLACEHOLDER.pack(side='left', padx=5, pady=5)
        self.URL_ENTRY = self.entry.create_content(self.URL_CONTAINER, 'url')
        self.URL_ENTRY.pack(side='right')

        '''
            Emplacement parametrage du telechargement :
                - Saisie nom du fichier
                - emplacement de stockage
                - Saisie type telechargement (mp3 ou mp4)
        '''
        self.SETTING_CONTAINER = self.labelframe.create_content('advanced_settings')
        self.SETTING_CONTAINER.pack(pady=30)
        self.LISTBOX = self.listbox.create_content(self.SETTING_CONTAINER, self.setting.get_settings_data('extensions'))
        self.LISTBOX.grid(pady=10, padx=20, row=0, column=0)
        self.BROWSE_BUTTON = self.button.create_browse_button(self.SETTING_CONTAINER, 'select_folder')
        self.BROWSE_BUTTON.configure(command=self.browse_forlder)
        self.BROWSE_BUTTON.grid(pady=10, row=0, column=1)
        self.FORMAT_LISTBOX = self.listbox.create_content(self.SETTING_CONTAINER, self.setting.get_settings_data("fomats"))
        self.FORMAT_LISTBOX.grid(row=0, column=2, pady=10)
        self.LISTBOX.bind("<<ComboboxSelected>>", self.dowload_video)
        self.NAME_PLACEHOLDER = self.label.create_placeholder(self.SETTING_CONTAINER, 'name')
        self.NAME_PLACEHOLDER.grid(pady=10, row=1, column=0)
        self.NAME_ENTRY = self.entry.create_content(self.SETTING_CONTAINER, 'name')
        self.NAME_ENTRY.grid(pady=10, row=1, column=1, columnspan=2)
        self.SUBMIT_BUTTON = self.button.create_submit_button(self.WINDOW, 'download')
        self.SUBMIT_BUTTON.configure(command=self.dowload_video)
        self.SUBMIT_BUTTON.pack(side='bottom', pady=25)
