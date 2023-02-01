from src.model.action.listable_action import ListableAction


class MoveToPosition(ListableAction):
    key: str = "move"

    def __init__(self, robot_nr: int, coordinates: dict, is_cartesian:bool) -> None:
        self.robot_nr = robot_nr
        self.coordinates = coordinates
        self.is_cartesian = is_cartesian



    def get_robot_nr(self) -> int:
        return self.robot_nr
    


    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = MoveToPosition.key
        to_return["robot_nr"] = self.robot_nr
        to_return["is_cartesian"] = self.is_cartesian
        to_return["coordiantes"] = self.coordinates
        return to_return