import requests
import datetime
import os
import logging
import argparse
import json

# Arguments
parser = argparse.ArgumentParser(description='Zeitraffer')
parser.add_argument('-loglevel', help='set loglevel', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO')
parser.add_argument('-config', help='config file. See TEMPLATE_config.json for a template ;).', default='config.json')

args = parser.parse_args()

# load config file
with open('config.json') as config_file:
    config = json.load(config_file)

# set loglevel
logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', filename='zeitraffer.log', encoding='UTF-8', level=getattr(logging, args.loglevel.upper()))

# get filetype from string
def get_filetype(string):
    return string.split(".")[-1]

# get image from URL and save it to file_name
def get_image(url, file_name):
    logging.info("Getting image from: " + url)
    r = requests.get(url)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)
            logging.info("Saved image to: " + file_name)
    else:
        logging.error("Could not get image from: " + url)

# create folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        logging.info("Creating folder: " + folder_name)
        os.makedirs(folder_name)   

# file_name is timestamp
file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

for cam in config["cams"]:
    create_folder(cam["folder"])
    file_type = get_filetype(cam["url"])
    get_image(cam["url"], cam["folder"] + "/" + file_name + '.' + file_type)