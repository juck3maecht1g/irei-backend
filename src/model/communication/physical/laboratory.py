from src.model.communication.physical.robot import Robot

class Laboratory:
    def __init__(self, name: str, robots: list[Robot]) -> None:
        self.name = name
        self.robots = robots

    def get_name(self) -> str:
        return self.name

    def get_robots(self) -> list[Robot]:
        return self.robots
        return [{
            "name": "robot",
            "ip": "1293.1239.12389"
        }]
