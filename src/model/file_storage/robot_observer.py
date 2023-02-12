from abc import ABC, abstractmethod


class RobotObserver(ABC):

    @abstractmethod
    def update_robot(self):
        pass