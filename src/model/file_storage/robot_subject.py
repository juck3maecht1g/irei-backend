from src.model.file_storage.robot_observer import RobotObserver


class RobotSubject():
    _observers: list[RobotObserver] = []

    def attach(self, observer: RobotObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: RobotObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update_robot()