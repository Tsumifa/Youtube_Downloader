# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    import pytube as _pytube
except Exception as e:
    raise e

# == LOGIC PART == #


class Download:

    def __init__(self):
        pass

    def download(self, url, extensions, name, directory):
        try:
            self.video_to_dowload = _pytube.YouTube(url)
            '''
                attribut comme nom a la video son titre si aucun nom est fourni
            '''
            if name == "":
                self.title = self.video_to_dowload.title()
            else:
                self.title = name
            
            '''
                determine le format de telechargement souhaite + meilleur qualite possible
            '''
            if extensions == 'video':
                self.format = 'mp4'
            else:
                self.format = 'mp3'

            self.possible_streams = self.video_to_dowload.streams.filter(file_extension=self.format, progressive=True).order_by('resolution')
            
            self.quality = self.possible_streams[-1]

            '''
                attribut un emplacement par defaut au fichier telecharge si aucun n'est fourni
            '''
            self.directory = directory

            try:
                self.quality.download(self.directory, filename=self.title)
            except Exception as e:
                return 1

        except _pytube.exceptions.RegexMatchError:
            return 1
