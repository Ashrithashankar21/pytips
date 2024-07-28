from typing import Any, Dict, List


def invert_dict(input_dict: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    # Initialize an empty dictionary for the inverted result
    inverted_dict = {}

    # Iterate over the items in the input dictionary
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = []
        # Append the key to the list of keys for this value
        inverted_dict[value].append(key)

    return inverted_dict


if __name__ == "__main__":
    input_dict = {
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 2,
        "e": 3,
    }
    inverted_result = invert_dict(input_dict)
    print(inverted_result)
