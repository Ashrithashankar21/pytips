import os
import json
from datetime import datetime

file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/standard_libraries/database.txt"
)


def database_manager(command: str, filename: str, data=None, record_id=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = None

    if command == "CREATE":
        if data is None:
            print(f"{timestamp} - CREATE failed: No data provided")
            return
        with open(filename, "a") as file:
            json_data = json.dumps(data)
            file.write(f"{json_data}\n")
        result = "Record created"

    elif command == "READ":
        records = []
        if not os.path.exists(filename):
            print(f"{timestamp} - READ failed: File does not exist")
            return []
        with open(filename, "r") as file:
            for line in file:
                records.append(json.loads(line.strip()))
        result = records

    elif command == "UPDATE":
        if record_id is None or data is None:
            print(f"{timestamp} - UPDATE failed")
            return
        updated = False
        if not os.path.exists(filename):
            print(f"{timestamp} - UPDATE failed: File does not exist")
            return
        temp_filename = f"{filename}.tmp"
        with open(filename, "r") as file, \
             open(temp_filename, "w") as temp_file:
            for line in file:
                record = json.loads(line.strip())
                if record.get("id") == record_id:
                    record.update(data)
                    updated = True
                temp_file.write(f"{json.dumps(record)}\n")
        os.replace(temp_filename, filename)
        result = "Record updated" if updated else "Record not found"

    elif command == "DELETE":
        if record_id is None:
            print(f"{timestamp} - DELETE failed: No record_id provided")
            return
        deleted = False
        if not os.path.exists(filename):
            print(f"{timestamp} - DELETE failed: File does not exist")
            return
        temp_filename = f"{filename}.tmp"
        with open(filename, "r") as file, \
             open(temp_filename, "w") as temp_file:
            for line in file:
                record = json.loads(line.strip())
                if record.get("id") != record_id:
                    temp_file.write(f"{json.dumps(record)}\n")
                else:
                    deleted = True
        os.replace(temp_filename, filename)
        result = "Record deleted" if deleted else "Record not found"

    else:
        print(f"{timestamp} - Invalid command")
        return

    print(f"{timestamp} - {result}")
    return result


if __name__ == "__main__":
    filename = file_path
    database_manager(
        "CREATE",
        filename,
        {"id": 4, "name": "David", "age": 28, "email": "david@example.com"},
    )
    print(database_manager("READ", filename))
    database_manager("UPDATE", filename, {"name": "Alice Smith"}, record_id=1)
    print(database_manager("READ", filename))
    database_manager("DELETE", filename, record_id=2)
    print(database_manager("READ", filename))
