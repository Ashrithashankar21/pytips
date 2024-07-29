import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        print(f"Execution time: {self.execution_time:.4f} seconds")


file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/context_managers/data.json"
)

if __name__ == "__main__":
    with Timer():
        total = 0
        for i in range(10**7):
            total += i
        print(f"Total: {total}")

    with Timer():
        with open(file_path, "w") as f:
            for i in range(10**5):
                f.write(f"Line {i}\n")

    import os

    os.remove(file_path)
