import unittest
from greeting import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice")
        self.assertEqual(greet(""), "Hello, Stranger")
        self.assertEqual(greet(None), "Hello, Stranger")

if __name__ == "__main__":
    unittest.main()
