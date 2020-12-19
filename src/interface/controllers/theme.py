# == IMPORTATIONS == #

try:
    #- Librairies
    import json
except Exception as e:
    raise e

# == LOGIC PART == #


class Theme:

    def __init__(self, file_path):
        with open('assets/themes/' + file_path + '.json', 'r') as theme_file:
            self.theme_data = json.load(theme_file)
 
    def get_theme(self, element):
        return str(self.theme_data[element])