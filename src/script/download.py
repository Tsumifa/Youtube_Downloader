# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    import pytube
except Exception as e:
    raise e

# == LOGIC PART == #


class Download:

    def __init__(self, url, quality, extensions, name, directory):
        self.url = url                  # Url of the video
        self.quality = quality          # Quality (1080 or 720)
        self.extensions = extensions    # mp3 or mp4
        self.name = name                # name of the file
        self.directory = directory      # directory where the file will be stored

    def download(self):
        pass

    def move_to_directory(self):
        pass