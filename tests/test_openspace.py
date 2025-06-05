import unittest
from models.person import Person
from models.table import Table
from models.openspace import OpenSpace
from io import StringIO
import sys

class TestOpenSpace(unittest.TestCase):

    def setUp(self):
        self.space = OpenSpace("BeCode Open Space")
        self.table1 = Table("T1", 2)
        self.table2 = Table("T2", 1)
        self.space.add_table(self.table1)
        self.space.add_table(self.table2)

        self.person1 = Person("Alice", "developer")
        self.person2 = Person("Bob", "coach")
        self.person3 = Person("Charlie", "designer")
        self.person4 = Person("Dave", "developer")  # Exceeds total capacity

    def test_add_table(self):
        self.assertEqual(len(self.space.tables), 2)
        self.assertIn(self.table1, self.space.tables)

    def test_assign_person_success(self):
        result = self.space.assign_person(self.person1)
        self.assertTrue(result)
        assigned = any(self.person1 in table.occupants for table in self.space.tables)
        self.assertTrue(assigned)

    def test_assign_person_failure_when_full(self):
        # Fill all tables
        self.space.assign_person(self.person1)
        self.space.assign_person(self.person2)
        self.space.assign_person(self.person3)

        # Try to add a 4th person when only 3 seats exist
        result = self.space.assign_person(self.person4)
        self.assertFalse(result)

    def test_display_output(self):
        self.space.assign_person(self.person1)
        self.space.assign_person(self.person2)

        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        self.space.display()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("BeCode Open Space", output)
        self.assertIn("Alice", output)
        self.assertIn("Bob", output)

if __name__ == '__main__':
    unittest.main()
