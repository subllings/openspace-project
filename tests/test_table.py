import unittest
from models.person import Person
from models.table import Table

class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = Table("Table A", 2)
        self.person1 = Person("Alice", "developer")
        self.person2 = Person("Bob", "coach")
        self.person3 = Person("Charlie", "designer")

    def test_add_person_success(self):
        added = self.table.add_person(self.person1)
        self.assertTrue(added)
        self.assertIn(self.person1, self.table.occupants)
        self.assertFalse(self.table.is_full())

    def test_add_person_until_full(self):
        self.table.add_person(self.person1)
        self.table.add_person(self.person2)
        self.assertTrue(self.table.is_full())

        added = self.table.add_person(self.person3)
        self.assertFalse(added)
        self.assertNotIn(self.person3, self.table.occupants)

    def test_remove_person(self):
        self.table.add_person(self.person1)
        self.table.remove_person(self.person1)
        self.assertNotIn(self.person1, self.table.occupants)
        self.assertFalse(self.table.is_full())

    def test_str_representation(self):
        self.table.add_person(self.person1)
        output = str(self.table)
        self.assertIn("Table A", output)
        self.assertIn("Alice (developer)", output)
        self.assertIn("1 free seats", output)

if __name__ == '__main__':
    unittest.main()
