from src.model.action.action import Action
from src.model.communication.physical.robot import Robot


class ActionList(Action):
    #sequential_key: str = "sequential_list"
    #parallel_key: str = "parallel_list"

    def __init__(self, name: str, key: str) -> None:
        self.name = name
        self.content: list[Action] = []
        self.key = key
      

    # switches places of two actions
    def swap(self, first: int, second: int) -> None:
        temp = self.content[first]
        self.content[first] = self.content[second]
        self.content[second] = temp


    def add_action(self, action: Action) -> None:
        self.content.append(action)

    
    def delete_action(self, pos: int) -> None:
        del self.content[pos]


    def get_content(self) -> list[Action]:
        return self.content
    

    def dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = self.key
        to_return["name"] = self.name
        content: list[Action] = []
        for action in self.content :
            content.append(action.dictify(robots))

        to_return["content"] = content
        return to_return
    
    def dictify_to_display(self, robots: list[Robot]) -> dict:

        return {"key": self.key, "name": self.name}