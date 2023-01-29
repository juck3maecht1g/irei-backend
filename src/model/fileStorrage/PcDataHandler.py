import os
import shutil
import pickle

class PcDataHandler:

    def __init__(self, root_path) -> None:
         self.root = root_path
         self.path = root_path
    
    def navigate_to_parent(self):
        if not (self.path == self.root):
            self.path = os.path.dirname(self.path)

    def navigate_to_child(self, name):
        if (name in self.list_children()):
            self.path = os.path.join(self.path, name)

    def get_dir_content(self):
        return os.listdir(self.path)


    def create_directory(self, name):
        if not (name in self.list_children()):
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