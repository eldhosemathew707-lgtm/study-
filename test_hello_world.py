import unittest
from hello_world import greet

class TestHelloWorld(unittest.TestCase):
    def test_greet_default(self):
        """Test default greeting when no argument is provided."""
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_custom_name(self):
        """Test personalized greeting with custom name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Eldhose"), "Hello, Eldhose!")

if __name__ == "__main__":
    unittest.main()
