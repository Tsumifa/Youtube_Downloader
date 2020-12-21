# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Files
    '''
        import pour front_end
    '''
    import interface.root as _root
    import interface.controllers.language as _language
    import interface.controllers.settings as _settings
    import interface.controllers.theme as _theme

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
            initialisation des classes controllers
        '''
        self.settings = _settings.Settings()
        self.language = _language.Language()
        self.theme = _theme.Theme()

        '''
            initialisation des classes script
        '''
        self.downloader = _download.Download()

# == START PROGRAM == #

if __name__ == "__main__":
    try:
        root = _root.Root()
    except ModuleNotFoundError:
        print('error')