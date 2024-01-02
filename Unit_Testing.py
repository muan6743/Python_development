import unittest

# Define your intermediate level practical program as a class
class MyProgram:
    def add_numbers(self, a, b):
        return a + b

# Create a test class that inherits from unittest.TestCase
class MyProgramTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of your practical program class
        self.program = MyProgram()

    def test_add_numbers(self):
        # Test the add_numbers method of your practical program
        result = self.program.add_numbers(2, 3)
        self.assertEqual(result, 5)

    # Add more test methods for other methods in your practical program

# Run the tests
if __name__ == '__main__':
    # Run the tests and print the message if all tests pass
    result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(MyProgramTest))
    if result.wasSuccessful():
        print("Test has been successfully passed.")
