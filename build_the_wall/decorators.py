from constants import NEW_LINE


def to_lists(func):
    """Remove the new lines and put each row to list"""

    def wrapper(input_file):
        data = func(input_file)
        return [item.replace(NEW_LINE, '').split() for item in data]
    return wrapper