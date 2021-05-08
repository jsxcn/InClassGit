import unittest
import name

class testCaseName(unittest.TestCase):
    def test_Person(self):
        person1 = name("Jennifer", "Hansen")
        person1 = name("Lucien")

    self.assertEqual(person1.fullname, "Tiffany Hansen")

    person1.first = "Liam"
    person1.last = "Bryant"

    self.assertEqual(person1.fullname, "Liam Bryant")

    self.assertEqual(person2.fullname, "Lucien")

if __name__ == "__main__":
    unittest.main()
