import unittest
import sqlite3
from unittest.mock import patch
import main

class TestStudentDatabase(unittest.TestCase):

    def setUp(self):
        # Initialize the database and test data
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        main.conn = self.conn  # Override the database connection in your code
        self.cursor.executescript("""
            -- Create test tables
            CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                password TEXT
            );
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                contact TEXT,
                ssn TEXT,
                student_number TEXT,
                image_path TEXT
            );
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY,
                student_id TEXT,
                course TEXT,
                grade TEXT
            );
            -- Add a test user
            INSERT INTO users (username, password) VALUES ('admin', 'password');
            -- Add a test student
            INSERT INTO students (name, contact, ssn, student_number, image_path)
            VALUES ('Test Student', 'test@example.com', '123-45-6789', 'S12345', 'test_image.png');
        """)

    def tearDown(self):
        # Close the in-memory database
        self.conn.close()

    @patch('builtins.input', side_effect=['admin', 'password'])  # Mock user input for login
    def test_login_successful(self, mock_input):
        # Test successful login with correct username and password
        result = main.login()
        self.assertEqual(result, "Login successful.")

    @patch('builtins.input', side_effect=['wrong_user', 'wrong_password'])  # Mock user input for login
    def test_login_incorrect_credentials(self, mock_input):
        # Test login with incorrect username and password
        result = main.login()
        self.assertEqual(result, "Incorrect username or password. Please try again.")


if __name__ == '__main__':
    unittest.main()
