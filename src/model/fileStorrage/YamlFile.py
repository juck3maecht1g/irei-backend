import os, yaml

import src.model.fileStorrage.FileInterface as FileInterface

class YamlConfig(FileInterface):

    def __write(self):
        with open(os.path.join(self.path, self.file_name), 'wb') as outfile:
            yaml.dump(self.data, outfile)

    def __read(self):
        with open(os.path.join(self.path, self.file_name), 'r') as infile:
            return yaml.safe_load(infile)




    