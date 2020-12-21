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
            settings_file.close()

    def get_settings_data(self, element):
        return str(self.settings_data[element])

    def change_setting(self, element, value):
        self.settings_data[element] = value
        print(type(self.settings_data))
        with open('assets\data\settings.json', 'w') as settings_file:
            settings_file.write(json.dumps(self.settings_data, indent=4, sort_keys=True))
        