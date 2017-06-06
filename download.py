# Programming practices in Python course in IBI HU Berlin
import requests
import os
import shutil

global dump

def download_file():
    global dump
    url = "https://moodle.hu-berlin.de/mod/folder/view.php?id=1122704"
    file = requests.get(url, stream=True)
    dump = file.raw

def save_file():
    global dump
    location = os.path.abspath("/Users/hsuan/Google\ Drive/Digital\ Curation_HU_Semester\ 2/Long\ Term\ Archiving/Slides")
    with open("file.gz", 'wb') as location:
        shutil.copyfileobj(dump, location)
    del dump
