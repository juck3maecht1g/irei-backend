import src.model.fileStorrage.YamlFile as YamlFile
import src.model.communication.physical.Laboratory as Laborartory
import src.model.communication.physical.Robot as Robot

class GlobalConfigHandler(YamlFile):

    def __init__ (self, file_name, path):
        data = {
            "Laboratories": {
                "Laboratory 1": {
                    "LabName": "",
                    "Robots": {
                        "Robot1": {
                            "name": "Coller Rob",
                            "ip": "101.10.20.101"
                        },
                        "Robot2": {
                            "name": "Coller Rob",
                            "ip": "101.10.20.101"
                        },
                        "Robot3": {
                            "name": "Coller Rob",
                            "ip": "101.10.20.101"
                        }
                    }
                },
            },

            "ActiveUser": "Max",
            "Users":{
                "Max": { 
                    "language": "english",
                },

                "Moritz": { 
                    "language": "german",
                }
            }
        }
        super.__init__(data, file_name, path)

    
    def get_language(self):
        active_user = self.data["ActiveUser"]
        return self.data[active_user]["language"]


    def get_labs(self):
        self.__read()
        return self.data["Laboratories"]

    def get_lab(self, lab_name):
        self.__read()
        lab = self.data["Laboratories"][lab_name]
        lab_rob = []

        for rob_data in lab:
            robot = Robot(rob_data["name"], rob_data["ip"])
            lab_rob.append(robot)

        return Laborartory(lab_name, lab_rob)
