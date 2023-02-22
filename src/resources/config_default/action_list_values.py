from enum import Enum


class AlValues(Enum):
    TYPE = "type"
    CONTENT = "content"
    DEFAULT_DATA = {TYPE: "", CONTENT: []}
    PARALLEL_TYPE = "parallel_list"
    SEQUENTIAL_TYPE = "sequential_list"

    FOLDER_NAME = "ActionLists"
    ERROR_FOLDER_NAME = "an ActionLists directory"
