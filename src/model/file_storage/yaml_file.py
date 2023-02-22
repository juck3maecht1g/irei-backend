import os
import yaml

from src.model.file_storage.file_interface import FileInterface


class YamlFile(FileInterface):

    def __init__(self, root: str, file_name: str , data: dict):
        super().__init__(root, file_name, ".yml", data)
        

    def write(self):
        with open(os.path.join(self.path, self.get_extended_name()), 'w') as outfile:
            yaml.dump(self.data, outfile, sort_keys=False,
                      default_flow_style=None)

    def read(self) -> dict:
        with open(os.path.join(self.path, self.get_extended_name()), 'r') as infile:
            self.data = yaml.safe_load(infile)

            
