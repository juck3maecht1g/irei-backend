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

    def map_dictify(self, map: dict) -> dict:
        sublist_nr = 0
        to_return = dict()
        to_return["key"] = self.key
        to_return["name"] = self.name
        tmp_content = []
        for action in self.content:
            if "list" in action.key:
                tmp_content.append(action.map_dictify(map["sublist"][sublist_nr]))
                sublist_nr += 1
            else:
                tmp_content.append(action.map_dictify(map))

        to_return["content"] = tmp_content

        return to_return
    
    def nr_dictify(self) -> dict:
        sublist_nr = 0
        to_return = dict()
        to_return["key"] = self.key
        to_return["name"] = self.name
        tmp_content = []
        for action in self.content:
            if "list" in action.key:
                tmp_content.append(action.nr_dictify())
                sublist_nr += 1
            else:
                tmp_content.append(action.nr_dictify())

        to_return["content"] = tmp_content

        return to_return

    def dictify_to_display(self, robots: list[Robot]) -> dict:
        return {"key": self.key, "name": self.name}


    def do_mapping(self):
        to_return = {"sublist" : []}
        for c in range(0, len(self.get_content())):
            if not isinstance(self.get_content()[c], ActionList):
                for nr in self.get_content()[c].robot_nrs:
                    if not nr in to_return.keys():
                        to_return |= ({nr: "none"})
            else:
                print(self.get_content()[c])
                to_return["sublist"].append(self.get_content()[c].do_mapping())

        return to_return