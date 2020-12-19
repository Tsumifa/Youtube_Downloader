# == IMPORTATIONS == #

try:
    #- Librairies
    import json
except Exception as e:
    raise e

# == LOGIC PART == #


class Language:

    def __init__(self, file_path):
        
        with open('assets/i18n/' + file_path + '.json') as language_file:
            self.language_data = json.load(language_file)

    def get_text(self, text_data):
        return str(self.language_data[text_data])