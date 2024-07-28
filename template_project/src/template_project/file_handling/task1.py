import os
import mmap

file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/file_handling/example.txt"
)


class Advanced_file_ops:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            buffer_size = self.optimize_Buffer()
            with open(self.file_path, "r", buffering=buffer_size) as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"The file {self.file_path} does not exist.")
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def write_file(self, data):
        try:
            buffer_size = self.optimize_Buffer()
            with open(self.file_path, "a", buffering=buffer_size) as file:
                file.write(data + "\n")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_large_file(self):
        try:
            file_size = os.path.getsize(self.file_path)
            if file_size > 1 * 1024 * 1024:
                with open(self.file_path, "r+b") as file:
                    mmapped_file = mmap.mmap(file.fileno(), 0)
                    for line in iter(mmapped_file.readline, b""):
                        print(line.strip().decode("utf-8"))
                    mmapped_file.close()
            else:
                self.read_file()
        except FileNotFoundError:
            print(f"The file {self.file_path} does not exist.")
        except IOError as e:
            print(f"An error occurred while handling the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def optimize_Buffer(self):
        try:
            file_size = os.path.getsize(self.file_path)
            if file_size < 10 * 1024:
                return 1024
            elif file_size < 100 * 1024:
                return 4096
            else:
                return 8192
        except FileNotFoundError:
            print(f"The file {self.file_path} does not exist.")
            return 1024
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 1024


file_ops = Advanced_file_ops(file_path)

file_ops.read_file()

file_ops.write_file("This is a test line.")

file_ops.handle_large_file()
