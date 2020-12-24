# Youtube_Downloader

**With this app you can download youtube videos (obviously...) with a few more options:**

- You can choose between audio & video : (mp3 or mp4).
- Moreover, you can decide to get anlo the audio or the images with the mp4.
- You can rename you file. If none is choosen, the script will rename it with the title of the video.
- You can select the storage location of your file. If none is choosen, the script will store it in Downloads.
- The script downloads the video with the highest quality possible.


**The infrastructure of the script :**

> Youtube_Downloader:
> |
> |--.idea
> |--assets
> |      |--data
> |      |      |--settings.json
> |      |--i18n
> |      |      |--fr.json
> |      |      |--en-us.json
> |      |--img
> |      |      |--logo.ico
> |      |--themes
> |             |--dark.json
> |             |--bright.json
> |--bin
> |      |--youtube_downloader.bat
> |      |--youtube_downloader.exe
> |--doc
> |      |--fr.html
> |      |--en-us.html
> |--src
> |      |--interface
> |      |       |--controllers
> |      |       |         |--language.py
> |      |       |         |--settings.py
> |      |       |         |--theme.py
> |      |       |--models
> |      |       |          |--alert.py
> |      |       |          |--button.py
> |      |       |          |--entry.py
> |      |       |          |--label.py
> |      |       |          |--labelframe.py
> |      |       |          |--listbox.py
> |      |       |          |--menu.py
> |      |       |--views
> |      |       |          |--about.py
> |      |       |          |--options.py
> |      |       |--root.py
> |      |--script
> |      |       |--download.py
> |      |--main.py
> |--.gitignore
> |--README.
>
> For the interface, this is an MVC infrastructure.
>

**The modules :**

- For the interface I used *tkinter*.

- For the json files, I used the integrated librairy *json*.

- To dowload the videos, I used *pytube*.
