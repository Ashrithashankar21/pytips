import unittest
import logging
from datetime import datetime
from task1 import Calculator


file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/unit_tests/log.txt"
)


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.test_start_time = datetime.now()
        self.log_file = file_path
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


if __name__ == "__main__":
    unittest.main()
