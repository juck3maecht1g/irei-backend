# outdated, to be removed
from src.model.action.action import Action
from src.model.communication.physical.robot import Robot

class ParallelActionList(Action):
    key: str = "parallel_action_list"

    def __init__(self, name: str) -> None:
        self.name = name
        self.content: list[list[Action]] = []
      

    # switches places of two positions 
    def swap(self, first_first: int,first_second:int, second_firs: int, second_second:int) -> None:
        temp = self.content[first_first][first_second]
        self.content[first_first][first_second] = self.content[second_firs][second_second]
        self.content[second_firs][second_second] = temp


    def add_action(self, action: Action, position:int) -> None:
        if position == -1:
            self.content.append(action)
        else :
            self.content[position].append(action)
    
    def delete_action(self, pos, pos_in_pos: int) -> None:
        if pos_in_pos != -1:
            del self.content[pos][pos_in_pos]
            if len(self.content[pos]) == 0:
                del self.content[pos]
        else:
            del self.content[pos]

    def get_content(self) -> list[Action]:
        return self.content
    

    def dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = ParallelActionList.key
        to_return["name"] = self.name
        content: list[list[Action]] = []
        for position in self.content :
            content.append([])
            for action in position: #adds all parallels for one position to list
                content[position].append(action.dictify(robots))

        to_return["content"] = content
        return to_return
    
    def dictify_to_display(self, robots: list[Robot]) -> dict:

        return {"key": self.key, "name": self.name}