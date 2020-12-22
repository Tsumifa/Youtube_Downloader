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
        self.menu = _menu.Menu(self.language, self.theme)
        self.label = _label.Create_Label(self.language, self.theme)
        self.labelframe = _labelframe.Labelframe(self.language, self.theme)
        self.entry = _entry.Entry(self.language, self.theme)

        '''
            initialisation des classes script
        '''
        #self.downloader = _download.Download()

        ''' 
            initialisation des classes interfaces
        '''
        self.root = _root.Root(self.settings, self.language, self.theme, self.menu, self.label, self.entry, self.labelframe)

# == START PROGRAM == #

if __name__ == "__main__":
    '''
        Initialisation de la classe parente
    '''
    main = Main()