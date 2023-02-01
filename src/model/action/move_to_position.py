from src.model.action.listable_action import ListableAction


class MoveToPosition(ListableAction):
    key: str = "move"

    def __init__(self, robot_nrs: list[int], coordinates: dict, type: str) -> None:
        super(robot_nrs)
        self.coordinates = coordinates
        self.type = type

    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = MoveToPosition.key
        to_return["robot_nrs"] = self.get_robot_nrs()
        to_return["type"] = self.type
        to_return["coordiantes"] = self.coordinates
        return to_return
