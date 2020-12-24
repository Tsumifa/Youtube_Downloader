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

    def download(self, url, extensions, name, directory, _format_option):
        try:
            self.video_to_dowload = _pytube.YouTube(url)
            
            '''
                determine le format de telechargement souhaite + meilleur qualite possible
            '''
            if extensions == 'video':
                self.format = 'mp4'
                self.format_option = _format_option

                '''
                    verifie si l'utilisateur veut uniquement son, video ou les deux
                '''
                if self.format_option == 'only_video':
                    self.possible_streams = self.video_to_dowload.streams.filter(file_extension=self.format, only_video=True).order_by('resolution')
                else:
                    self.possible_streams = self.video_to_dowload.streams.filter(file_extension=self.format, progressive=True).order_by('resolution')

                if str(self.possible_streams) == '[]':
                    return 2
                else:
                    self.quality = self.possible_streams[-1]

            else:
                self.format = 'mp3'
                self.possible_streams = self.video_to_dowload.streams.filter(only_audio=True)
                if str(self.possible_streams) == '[]':
                    return 2
                self.quality = self.possible_streams[0]

            '''
                attribut un emplacement par defaut au fichier telecharge si aucun n'est fourni
            '''
            self.directory = directory

            try:
                if name == "":
                    self.quality.download(self.directory)
                else:
                    self.title = name
                    self.quality.download(self.directory, filename=self.title)
                return 0
            except Exception as e:
                return 1

        except _pytube.exceptions.RegexMatchError:
            return 1
