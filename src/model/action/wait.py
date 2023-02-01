from src.model.action.listable_action import ListableAction


class Wait(ListableAction):
    key: str = "wait"

    def __init__(self, robot_nrs: list[int], time: int) -> None: 
        super(robot_nrs)
        self.time = time

    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = Wait.key
        to_return["robot_nrs"] = self.get_robot_nrs()
        to_return["time"] = self.time
        return to_return
