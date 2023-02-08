import os
import yaml

from src.model.file_storage.file_interface import FileInterface


class YamlFile(FileInterface):

    def write(self):
        with open(os.path.join(self.path, self.file_name), 'w') as outfile:
            yaml.dump(self.data, outfile, sort_keys=False,
                      default_flow_style=None)

    def read(self):
        with open(os.path.join(self.path, self.file_name), 'r') as infile:
            self.data = yaml.safe_load(infile)
