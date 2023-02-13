from src.model.file_storage.path_observer import PathObserver


class PathSubject():
    _observers: list[PathObserver] = []

    def attach(self, observer: PathObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: PathObserver) -> None:
        self._observers.remove(observer)

    def notify(self, path: str) -> None:
        for observer in self._observers:
            observer.update_path(path)
