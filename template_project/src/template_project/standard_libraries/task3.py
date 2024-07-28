import os
import sys


def system_navigator(directory_path: str) -> dict:
    # Step 3: Initialize an empty dictionary to store file counts
    file_counts = {}

    # Step 2: Use os.walk to iterate over all directories and sub-directories
    for root, dirs, files in os.walk(directory_path):
        file_counts[root] = len(files)

    # Step 4: Use sys module to fetch system information
    system_info = {
        "python_version": sys.version,
        "platform": sys.platform,
    }

    return {"file_counts": file_counts, "system_info": system_info}


if __name__ == "__main__":
    directory_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    result = system_navigator(directory_path)
    print(result)
