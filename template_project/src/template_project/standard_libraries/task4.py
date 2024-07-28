import json

file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/standard_libraries/data.json"
)


def flatten_json(nested_json, parent_key="", sep="."):
    """Flatten a nested json object."""
    items = []
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def count_keys_by_depth(nested_json, depth=0, depth_counts=None):
    """Count the number of keys at each depth level."""
    if depth_counts is None:
        depth_counts = {}
    if depth not in depth_counts:
        depth_counts[depth] = 0
    depth_counts[depth] += len(nested_json)

    for k, v in nested_json.items():
        if isinstance(v, dict):
            count_keys_by_depth(v, depth + 1, depth_counts)

    return depth_counts


def json_analyzer(filename: str) -> dict:
    # Step 2: Read the JSON file and convert its content to a Python object
    with open(filename, "r") as file:
        data = json.load(file)

    # Step 3: Flatten the JSON
    flattened_json = flatten_json(data)

    # Step 4: Calculate the count of keys at each depth level
    depth_counts = count_keys_by_depth(data)

    # Return both the flattened JSON and the depth counts
    return {"flattened_json": flattened_json, "depth_counts": depth_counts}


if __name__ == "__main__":
    result = json_analyzer(file_path)
    print(result)
