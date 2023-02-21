from enum import Enum


class action_list(Enum):
    TYPE = "type"
    CONTENT = "content"
    DEFAULT_DATA = {TYPE: "",
            CONTENT: []}

    PARALLEL_TYPE = "parallel_list"
    SEQUENTIAL_TYPE = "sequential_list"
