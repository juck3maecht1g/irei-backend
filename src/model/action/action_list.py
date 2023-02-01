from src.model.action.action import Action


class ActionList(Action):
    key: str = "action_list"

    def __init__(self, name: str) -> None:
        self.name = name
        self.content: list[Action] = []
      

    # switches places of two actions
    def swap(self, first: Action, second: Action) -> None:
        temp = self.content[first]
        self.content[first] = self.content[second]
        self.content[second] = temp


    def add_action(self, action: Action) -> None:
        self.content.append(action)


    def get_content(self) -> list[Action]:
        return self.content
    

    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = ActionList.key
        to_return["name"] = self.name
        content: list[Action] = []
        for action in self.content :
            content.append(action.dictify())

        to_return["content"] = content
        return to_return