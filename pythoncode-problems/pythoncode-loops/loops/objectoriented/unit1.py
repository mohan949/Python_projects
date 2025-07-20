import unittest
from p1 import Programmer  # Assuming the class Programmer is in a module named your_module

class TestProgrammer(unittest.TestCase):
    def test_attributes(self):
        # Test case description: Ensure that the Programmer object is initialized with the correct attributes
        programmer = Programmer('Mohan', 110, 10)
        self.assertEqual(programmer.name1, 'Mohan')
        self.assertEqual(programmer.pin, 110)
        self.assertEqual(programmer.salary, 10)
        # Expected outcome: The attributes are correctly assigned to the Programmer object

    def test_get_name(self):
        programmer = Programmer('Shyam', 110, 10)
        self.assertEqual(programmer.get_name(), 'Shyam')

    def test_company_attribute(self):
        # Test case description: Ensure the class attribute 'company' is correctly set and accessible
        programmer = Programmer('Mohan', 110, 10)
        self.assertEqual(Programmer.company, 'Mircosoft')
        # Expected outcome: The 'company' class attribute should be 'Mircosoft'

    def test_designation_attribute(self):
        # Test case description: Ensure the class attribute 'designation' is correctly set and accessible
      #  programmer = Programmer('Mohan', 110, 10)
        self.assertEqual(Programmer.designation, 'SDE')
        # Expected outcome: The 'designation' class attribute should be 'SDE'

if __name__ == '__main__':
    unittest.main()

