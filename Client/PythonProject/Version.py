# coding=utf-8
from datetime import datetime
from Modul import create_a_new_folder, create_new_file, write_to_file
import os


class Version:

    # אתחול תיקייה של commit עם name ו-details

    def __init__(self, path, name, message):
        self.name = name
        self.message = message
        message += "{}-{}".format(self.name, datetime.now().strftime('%d-%m-%y-%H-%M-%S'))
        self.dir_path = os.path.join(path, name)
        create_a_new_folder(path, name)
        create_new_file(self.dir_path, 'details')
        file_path = os.path.join(self.dir_path, 'details')
        write_to_file(file_path, message + "\t" + name)
