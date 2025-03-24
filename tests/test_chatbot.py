"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

__author__ = "Nicholas Javier"
__version__ = "1.0.2025"

from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import get_account_number, get_amount

class TestChatbot(TestCase):
    """Unit tests for chatbot functions."""

    def test_get_account_number_type_error(self):
        """
        Test that a TypeError is raised when non-integer input is provided.
        """
        # Arrange
        with patch('builtins.input', return_value='non_numeric_data'):
            # Act and Assert
            with self.assertRaises(TypeError) as context:
                get_account_number()
            self.assertEqual(str(context.exception), "Account number must be an int type.")

    def test_get_account_number_value_error(self):
        """
        Test that a ValueError is raised when the account number does not exist.
        """
        # Arrange
        with patch('builtins.input', return_value='112233'):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account_number()
            self.assertEqual(str(context.exception), "Account number entered does not exist.")

    def test_get_account_number_valid(self):
        """
        Test that a valid account number is returned when correct input is given.
        """
        # Arrange
        with patch('builtins.input', return_value='123456'):
            # Act
            result = get_account_number()
            # Assert
            self.assertEqual(result, 123456)

    def test_get_amount_type_error(self):
        """
        Test that a TypeError is raised when non-numeric input is provided.
        """
        # Arrange
        with patch('builtins.input', return_value='abc'):
            # Act and Assert
            with self.assertRaises(TypeError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Amount must be a numeric type.")

    def test_get_amount_zero_value_error(self):
        """
        Test that a ValueError is raised when the amount entered is zero.
        """
        # Arrange
        with patch('builtins.input', return_value='0'):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Amount must be a value greater than zero.")

    def test_get_amount_negative_value_error(self):
        """
        Test that a ValueError is raised when the amount entered is negative.
        """
        # Arrange
        with patch('builtins.input', return_value='-50'):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Amount must be a value greater than zero.")

    def test_get_amount_valid(self):
        """
        Test that a valid amount is returned when correct input is given.
        """
        # Arrange
        with patch('builtins.input', return_value='100.50'):
            # Act
            result = get_amount()
            # Assert
        self.assertEqual(result, 100.50)

if __name__ == '__main__':
    main()
