# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Files
    '''
        import pour front_end
    '''
    #- controllers
    import interface.root as _root
    import interface.controllers.language as _language
    import interface.controllers.settings as _settings
    import interface.controllers.theme as _theme

    #- models
    import interface.models.menu as _menu
    import interface.models.label as _label
    import interface.models.labelframe as _labelframe
    import interface.models.entry as _entry
    import interface.models.listbox as _listbox
    import interface.models.button as _button
    import interface.models.alert as _alert

    #- views
    import interface.views.options as _options
    import interface.views.about as _about

    '''
        import pour back_end
    '''
    import script.download as _download

except Exception as e:
    raise e

# == LOGIC PART == #


class Main:

    def __init__(self):
        '''
            initialisation des classes front_end
        '''
        #- controllers
        self.settings = _settings.Settings()
        self.language = _language.Language(self.settings.get_settings_data("language"))
        self.theme = _theme.Theme(self.settings.get_settings_data("theme"))
    
        #- models
        self.label = _label.Create_Label(self.language, self.theme)
        self.labelframe = _labelframe.Labelframe(self.language, self.theme)
        self.entry = _entry.Entry(self.language, self.theme)
        self.listbox = _listbox.Listbox(self.language, self.theme)
        self.button = _button.Button(self.language, self.theme)
        self.alert = _alert.Alert(self.language, self.theme)

        #- views
        self.option_window = _options.Options_Window(self.settings, self.language, self.theme, self.listbox, self.label, self.button, self.alert)
        self.about_window = _about.About_Window(self.settings, self.language, self.theme, self.label)

        #- models - menu
        self.menu = _menu.Menu(self.language, self.theme, self.option_window, self.about_window)


        '''
            initialisation des classes script
        '''
        self.downloader = _download.Download()

        ''' 
            initialisation des classes interfaces
        '''
        self.root = _root.Root(self.settings, self.language, self.theme, self.menu, self.label, self.entry, self.labelframe, self.listbox, self.button, self.option_window, self.alert, self.downloader)

# == START PROGRAM == #

if __name__ == "__main__":
    '''
        Initialisation de la classe parente
    '''
    main = Main()
    