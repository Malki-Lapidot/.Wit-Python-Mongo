import os
import shutil
from datetime import datetime

from Modul import create_a_new_folder, copy_content_of_folder, replace_files_from_folder, delete_content_of_folder,initialize_current_version
from Version import Version

class Repository:

    def __init__(self):
        self.count_commit = 0
        path = os.path.join(os.getcwd(), '.wit')
        if not os.path.exists(os.path.join(path, 'staging')):
            create_a_new_folder(path, 'staging')
        if not os.path.exists(os.path.join(path, 'commiting')):
            create_a_new_folder(path, 'commiting')
        if not os.path.exists(os.path.join(path, 'current version')):
            current_version = Version(path, 'current version', 'first version')
        self.path_commiting = os.path.join(path, 'commiting')
        self.path_staging = os.path.join(path, 'staging')
        self.path_current_version = os.path.join(path, 'current version')
        initialize_current_version(os.getcwd(),self.path_current_version)

    def add(self, path):
        if os.path.isfile(path):
            shutil.copy(path, self.path_staging)
            print('The file added successfully')
        else:
            print('Path is not file')

    def commit(self, message):
        if os.listdir(self.path_staging):
            self.count_commit += 1
            name = str(self.count_commit)
            new_version = Version(self.path_commiting, name, message)
            copy_content_of_folder(self.path_current_version, new_version.dir_path)
            replace_files_from_folder(self.path_staging, new_version.dir_path)
            delete_content_of_folder(self.path_current_version)
            copy_content_of_folder(new_version.dir_path, self.path_current_version)
            print('The version commiting successfully')
        else:
            print('The staging is empty')

    def log(self):
        list_files = os.listdir(self.path_commiting)
        for file_name in list_files:
            print("file name: "+file_name)
            commit_path=os.path.join(self.path_commiting, file_name)
            with open(os.path.join(commit_path, 'details'), 'r') as my_file:
                print("message: "+my_file.readline()+"\n")

    def status(self):
        if os.listdir(self.path_staging):
            print('You can make commit')
        else:
            print('The staging is empty')

    def checkout(self,commit_id):
        my_path = os.path.join(self.path_commiting, commit_id)
        if not os.path.exists(my_path):
            print('The commit does not exist')
        else:
            delete_content_of_folder(self.path_current_version)
            copy_content_of_folder(my_path, self.path_current_version)




