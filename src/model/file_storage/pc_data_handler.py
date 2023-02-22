import os
import shutil
import pickle

from src.model.file_storage.path_subject import PathSubject


class PcDataHandler(PathSubject):

    def __init__(self, root_path) -> None:
        self.root = root_path
        self.path = root_path

    def navigate_to_parent(self):
        if not (self.path == self.root):
            self.path = os.path.dirname(self.path)
            self.notify(self.path)

    def navigate_to_child(self, name):
        if (name in self.get_dir_content()):
            self.path = os.path.join(self.path, name)
            self.notify(self.path)

    def is_exp(self) -> bool:
        return "experiment_config.yml" in os.listdir(self.path)

    def get_sub_dir(self):
        return list(filter(lambda x: os.path.isdir(os.path.join(self.path, x)), os.listdir(self.path)))

    def get_dir_content(self):
        return os.listdir(self.path)

    def create_directory(self, name):
        if not name in self.get_dir_content():
            new_dir = os.path.join(self.path, name)
            os.mkdir(new_dir)

    def save_log(self, file_name, data):
        with open(os.path.join(self.path, file_name), 'wb') as f:
            pickle.dump(data, f)


    def delete_directory(self, name):
        remove_path = os.path.join(self.path, name)
        shutil.rmtree(remove_path)

    def delete_file(self, name):
        remove_path = os.path.join(self.path, name)
        os.remove(remove_path)

    def delete_all_content(self):
        self.delete_directory("")
        os.mkdir(self.path)

    def get_path(self):
        return self.path
    
    def get_root(self):
        return self.root
