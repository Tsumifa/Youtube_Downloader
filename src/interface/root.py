# == IMPORTATIONS == #

try:
    #- Librairies
    import tkinter as tk

    #- Files
    import controllers.settings as settings
    import controllers.language as languages
    import controllers.theme as themes

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

root = Root()
print(root.theme.get_theme("backgroundColor"))
print(root.language.get_text("title"))
