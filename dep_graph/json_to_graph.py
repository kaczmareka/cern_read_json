import json
from collections import OrderedDict


def json_to_graph_function(
    file_path: str
) -> str:
    """
    Function that converts a json file to a dependency graph.
    Args:
        file_path (str): path to the json file.
    """

    def recursively_add_names(
        values: list, 
        indent: int, 
        to_print: str
    ) -> str:
        """
        Function that recursively adds the names of the packages 
        and dependencies to the string to be printed.
        Args:
            values (list): list of dependencies.
            indent (int): number of spaces to indent the current 
            dependency.
            to_print (str): string to be printed.
        """

        for value in values:
            # Check if the current dependency has dependencies.
            if value in keys:
                to_print += str("  "*indent + f"-{value}" + "\n")
                indent += 1
                # Recursively add the dependencies of the current dependency.
                to_print = recursively_add_names(ordered_json_content[value],
                                                 indent, to_print)
                indent -= 1
            else:
                to_print += str("  "*indent + f"-{value}" + "\n")
        return to_print

    # Read the json file.
    with open(file_path) as json_file:
        json_content = json.load(json_file)
    # Convert dictionary to OrderedDict to preserve the order of the keys.
    ordered_json_content = OrderedDict(json_content)
    # Get the keys of the dictionary.
    keys = list(ordered_json_content.keys())
    to_print = ""
    indent = 0
    # Add the names of the packages and dependencies to the string.
    to_print = recursively_add_names(keys, indent, to_print)
    # Remove the last newline character.
    to_print = to_print[:-1]
    # Return the string to be printed.
    return to_print
