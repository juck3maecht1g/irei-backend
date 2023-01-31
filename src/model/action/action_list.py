
class ActionList:
    key :str = "action_list"
    #name:str
    #content = []

    def __init__ (self, name :str): 
        self.key = ActionList.key
        self.name = name
        self.contend = []
      

    # switches places of two actions
    def swap (self, first, second):
        temp = self.contend[first]
        self.contend[first] = self.contend[second]
        self.contend[second] = temp


    def add_action(self, action):
        self.contend.append(action)

    def get_content(self):
        return self.contend
    


    def dictify (self):
        to_return = dict()
        to_return["key"] = self.key
        to_return["name"] = self.name
        content = []
        for action in self.contend :
            content.append(action.dictify())

        to_return["content"] = content
        return to_return