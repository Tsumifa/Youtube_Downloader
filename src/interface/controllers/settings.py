# == IMPORTATIONS == #

try:
    #- Librairies
    import json
except Exception as e:
    raise e

# == LOGIC PART == #


class Settings:

    def __init__(self):
        with open('assets\data\settings.json') as settings_file:
            self.settings_data = json.load(settings_file)

    def get_settings_data(self, element):
        return str(self.settings_data[element])
