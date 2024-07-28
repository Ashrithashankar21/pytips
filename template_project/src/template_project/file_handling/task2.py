from task1 import Advanced_file_ops
import os
import mmap


class Log_aggregator(Advanced_file_ops):
    def __init__(self, log_dir, output_file):
        self.log_dir = log_dir
        self.output_file = output_file
        super().__init__(output_file)

    def aggregate_logs(self):
        try:
            with open(self.output_file, "w") as outfile:
                for log_file in os.listdir(self.log_dir):
                    log_file_path = os.path.join(self.log_dir, log_file)
                    if os.path.isfile(log_file_path):
                        self._read_and_write_log(log_file_path, outfile)
        except Exception as e:
            print(f"An error occurred while aggregating logs: {e}")

    def _read_and_write_log(self, log_file_path, outfile):
        try:
            file_size = os.path.getsize(log_file_path)
            if file_size > 1 * 1024 * 1024:
                with open(log_file_path, "r+b") as log_file:
                    mmapped_file = mmap.mmap(log_file.fileno(), 0)
                    for line in iter(mmapped_file.readline, b""):
                        outfile.write(line.decode("utf-8"))
                    mmapped_file.close()
            else:
                buffer_size = self.optimize_Buffer()
                with open(log_file_path, "r", buffering=buffer_size) as log_file:
                    for line in log_file:
                        outfile.write(line)
        except FileNotFoundError:
            print(f"The log file {log_file_path} does not exist.")
        except PermissionError:
            print(f"Permission denied for the log file {log_file_path}.")
        except Exception as e:
            print(
                f"An error occurred while processing the log file {log_file_path}: {e}"
            )


log_dir = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/file_handling/logs"
)
output_file = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/file_handling/logs/aggregate_logs.txt"
)

log_aggregator = Log_aggregator(log_dir, output_file)

log_aggregator.aggregate_logs()
