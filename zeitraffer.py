import requests
import datetime
import os

cams = {
    "cam1": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
    "cam2": "https://www.python.org/static/img/python-logo.png"
}

# file_name is timestamp + .png
file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# get filetype from string
def get_filetype(string):
    return string.split(".")[-1]

# get image from URL and save it to file_name
def get_image(url, file_name):
    r = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(r.content)

# create folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)   

for cam, url in cams.items():
    create_folder(cam)
    file_type = get_filetype(url)

    get_image(url, cam + "/" + file_name + '.' + file_type)