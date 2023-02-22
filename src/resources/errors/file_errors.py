class FileNotAllowedInRootError(Exception):
    #Exception raised if attempting to write an experiment specific file in the root path.

    def __init__(self, name: str, root_path: str, message= "There can't be {name} in your root path: {root_path}"):
        super().__init__(message.format(name = name, root_path = root_path))

class FileNotExistsError(FileNotFoundError):
    #Exception raised if attempting to read a file that does not exists.

    def __init__(self, name: str, path: str, message= "There is no {name} in {path}."):
        super().__init__(message.format(name = name, path = path))

class FileNameAlreadyUsedError(FileExistsError):
    #Exception raised if attempting to read a file that does not exists.

    def __init__(self, name: str, path: str, message= "The name: {name} is already used in {path}."):
        super().__init__(message.format(name = name, path = path))


class RootHasNoParentError(Exception):
     #Exception raised if attempting to navigate to parent from root

    def __init__(self, message= "You can't navigate up from root."):
        super().__init__(message)


    