class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.entry_count = 0

    def __call__(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{self.entry_count}: {message}\n")
        self.entry_count += 1


file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/magic_methods/data.json"
)

if __name__ == "__main__":
    import os

    log_file = file_path

    if os.path.exists(log_file):
        os.remove(log_file)

    logger = Logger(log_file)

    logger("First log entry")
    logger("Second log entry")
    logger("Third log entry")

    with open(log_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    print(f"Entry count: {logger.entry_count}")

    os.remove(log_file)
