# Kodi-MAL-RPC-Discord

Do you want a simple python script that'll give your discord community an idea about what show you're watching in Kodi and/or give them an overview of your MyAnimeList statistics ? If the answer is yes you're on the right place.

Right now this script has been tested only in linux with Python 3.6+, any environment other than this one hasn't been tested.
You also need to know that i've targeted only **TV SHOWS**, still didn't have time to work on **Movies** section, **Live TV** or **Music** :( 

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)


# Prerequisites

You need to :
* Install Python3.6+.
* Install python dependencies (pip -i dependencies.txt).
* Discord Desktop app should be installed and running.
* Create your own application in the [DEVELOPER PORTAL](https://discordapp.com/developers/applications/), you can customize your app there (add image, icons, ...).

# How to use it
If you want the version without MyAnimelist Statistics support in Rich Presence download `UpdateStatus.py`, else download `UpdateStatuswithMyAnimeList.py`

* Grab your app Client-id and override myclientid variable in the following line : ```client_id = 'mysecretid'``` with your client-id.
* Replace myusername in python script : `username = 'myusername'` with your MyAnimeList Username (If you use UpdateStatuswithMyAnimeList.py)
* Enable your web UI in Kodi (basically your 8080 port as it is done by adding a web interface for Kodi).
* Play your content in **TV SHOWS**.
* execute the script ```python3.6 UpdateStatus.py``` (or ```python3.6 UpdateStatus.py &``` to run in background mode
* To kill your script ```kill -9 mypid``` (mypid is the pid's script whenever it's run in the background)

# Screenshot

![Alt text](Screenshot-uploaded.png?raw=true "Happy Update !")


# Enjoy

If you like this content you're welcome to watch, star or fork ;)
