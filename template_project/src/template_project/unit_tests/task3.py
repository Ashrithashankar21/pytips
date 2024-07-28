import math
from task1 import Calculator


class Calculator(Calculator):

    def advanced_operation(self, operation: str, number: float) -> float:
        if operation == "sqrt":
            return math.sqrt(number)
        elif operation == "log":
            return math.log(number)
        else:
            raise ValueError(f"Unsupported operation: {operation}")
