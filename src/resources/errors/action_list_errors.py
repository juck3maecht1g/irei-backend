class IndexOutOfBoundsError(Exception):
    #Exception raised if attempting to write an experiment specific file in the root path.

    def __init__(self, indices: list[int], list_length: int):
        if min(indices) < 0:
            message = f"You can't have a negative index in a list. Your index {min(indices)}."
        else:
            message = f"There is no index {max(indices)}. The highest index that is stored is {list_length - 1}."
        super().__init__(message)