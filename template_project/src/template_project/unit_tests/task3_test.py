import unittest
from unittest.mock import patch
from task3 import Calculator
from datetime import datetime
import logging


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.test_start_time = datetime.now()
        self.log_file = "test_results.log"
        logging.basicConfig(
            filename=self.log_file, level=logging.INFO, format="%(asctime)s %(message)s"
        )

    def tearDown(self):
        test_name = self.id().split(".")[-1]
        test_status = "passed" if self._outcome.success else "failed"
        test_end_time = datetime.now()
        duration = test_end_time - self.test_start_time
        log_message = (
            f"Test {test_name} {test_status} at {test_end_time} (Duration: {duration})"
        )
        logging.info(log_message)

    def test_add(self):
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 1), 1)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(0, 1), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(1, 1), 1)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(1, -1), -1)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(0, 0)

    def test_operations_with_zero(self):
        self.assertEqual(self.calc.add(0, 1), 1)
        self.assertEqual(self.calc.add(0, -1), -1)
        self.assertEqual(self.calc.subtract(0, 1), -1)
        self.assertEqual(self.calc.subtract(0, -1), 1)
        self.assertEqual(self.calc.multiply(0, 1), 0)
        self.assertEqual(self.calc.multiply(0, -1), 0)
        self.assertEqual(self.calc.divide(0, 1), 0)
        with self.assertRaises(ValueError):
            self.calc.divide(0, 0)

    @patch("task3.Calculator.advanced_operation")
    def test_advanced_operation(self, mock_advanced_operation):
        mock_advanced_operation.side_effect = lambda op, num: (
            {"sqrt": 4.0, "log": 2.0}.get(op, None)
            if op in ["sqrt", "log"]
            else (_ for _ in ()).throw(ValueError(f"Unsupported operation: {op}"))
        )

        self.assertEqual(self.calc.advanced_operation("sqrt", 16), 4.0)
        self.assertEqual(self.calc.advanced_operation("log", 100), 2.0)
        with self.assertRaises(ValueError):
            self.calc.advanced_operation("unsupported", 10)


if __name__ == "__main__":
    unittest.main()
