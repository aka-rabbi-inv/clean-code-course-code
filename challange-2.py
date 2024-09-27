# (c) Fazle Rabbi

from os import path, makedirs
from pathlib import Path


class Disk:
    def __init__(self, directory_name):
        self.directory_name = directory_name

    def get_directory_path(self):
        return Path(self.directory_name)

    def create_directory_if_not_exists(self):
        if (not path.exists(self.get_directory_path())):
            makedirs(self.directory_name)

    def insert_file(self, file_name, content):
        self.create_directory_if_not_exists()
        file_path = self.get_directory_path() / file_name
        file = open(file_path, 'w')
        file.write(content)
        file.close()
        # Todo: Add proper error handling


storage = Disk('logs')
storage.insert_file('test.txt', 'Test')
