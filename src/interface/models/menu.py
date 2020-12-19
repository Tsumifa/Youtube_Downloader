# == IMPORTATIONS == #

try:

    #- Librairies
    import tkinter as tk

except Exception as e:
    raise e

# == LOGIC PART == #


class Menu:

    def __init__(self, parent):
        
        self.option_text = 'hello'
        self.help_text = 'goodbye'
        self.parent = parent

        '''
            creation du widget menu
        '''
        self.menu = Menu(self.parent)

        '''
            creation des differentes fonctions du menu
        '''

        self.mainmenu.add_command(label=self.option_text, command=self.save)  
        self.mainmenu.add_command(label=self.help_text, command=self.help)

    def file(self):
        #Code to be written
        pass
 
    def help(self):
        #Code to be written
        pass   
 