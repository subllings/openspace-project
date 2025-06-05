import unittest
from models.person import Person

class TestPerson(unittest.TestCase):

    def test_create_person(self):
        # Create a Person object
        person = Person("Alice", "developer")

        # Check attributes
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.role, "developer")

    def test_str_representation(self):
        person = Person("Bob", "coach")
        self.assertEqual(str(person), "Bob (coach)")

if __name__ == '__main__':
    unittest.main()
