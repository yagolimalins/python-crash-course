import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.yago = Employee('yago', 'lima', 65000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.yago.give_raise()
        self.assertEqual(self.yago.salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.yago.give_raise(10000)
        self.assertEqual(self.yago.salary, 75000)

if __name__ == '__main__':
    unittest.main()