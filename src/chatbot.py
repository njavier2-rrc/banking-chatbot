"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "COMP-1327 Faculty"
__version__ = "1.0.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def get_account_number() -> int:
    """
    Prompts the user to enter their account number, validates it, and 
    returns the account number as an integer.

    Returns:
        int: The valid account number entered by the user.

    Raises:
        TypeError: If the input cannot be converted to an integer.
        ValueError: If the account number does not exist in the ACCOUNTS
        dictionary.
    """
    account_input = input("Please enter your account number: ")
    try:
        account_number = int(account_input)
    except ValueError:
        raise TypeError("Account number must be an int type.")

    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")

    return account_number

def get_amount() -> float:
    """
    Prompts the user to enter an amount to deposit, validates it, and
    returns the amount as a float.

    Returns:
        float: The valid amount entered by the user.

    Raises:
        TypeError: If the input cannot be converted to a numeric type.
        ValueError: If the amount is zero or a negative value.
    """
    amount_input = input("Enter an amount: ")
    try:
        amount = float(amount_input)
    except ValueError:
        raise TypeError("Amount must be a numeric type.")

    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")

    return amount

def get_balance(account_number: int) -> str:
    """
    Returns the balance message for the specified account number.

    Parameters:
        account_number (int): The account number to check.

    Returns:
        str: The balance message formatted as currency.

    Raises:
        TypeError: If the account number is not an int type.
        ValueError: If the account number does not exist in ACCOUNTS.
    """
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")

    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")

    balance = ACCOUNTS[account_number]["balance"]
    return f"Your current balance for account {account_number} is ${balance:,.2f}."

def make_deposit(account_number: int, amount: float) -> str:
    """
    Increases the bank account's balance by the specified amount.

    Parameters:
        account_number (int): The account number of the bank account.
        amount (float): The amount to deposit.

    Returns:
        str: The deposit confirmation message.

    Raises:
        TypeError: If account_number is not an int.
        ValueError: If the account number does not exist.
        ValueError: If the amount is not numeric or less than or equal 
        to zero.
    """
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")

    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")

    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a numeric type.")

    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")

    ACCOUNTS[account_number]['balance'] += amount

    return f"You have made a deposit of ${amount:,.2f} to account {account_number}."

def get_task() -> str:
    """
    Prompts the user to enter a task, validates it, and returns the task 
    in lowercase.

    Returns:
        str: The valid task entered by the user in lowercase.

    Raises:
        ValueError: If the task entered is not in the VALID_TASKS list.
    """
    task_input = input("What would you like to do (balance/deposit/exit)?: ")
    task = task_input.lower()

    if task not in VALID_TASKS:
        raise ValueError(f'"{task_input}" is an unknown task.')

    return task

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

COMPANY_NAME = "PiXELL River Financial"

# Print welcome message
print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! Let's get chatting!")

# Loop to continuously prompt the user for tasks until they exit
while True:
    try:
        # Get the task from user input (balance/deposit/exit)
        task = get_task()

        # Check if task is exit
        if task == 'exit':
            # Print thank you message
            print(f"Thank you for banking with {COMPANY_NAME}.")
            break

        # Get the account number
        account_number = get_account_number()

        # Check if task is deposit
        if task == 'deposit':
            # Get the amount to deposit
            amount = get_amount()
            # Make the deposit
            deposit_message = make_deposit(account_number, amount)
            # Print deposit message
            print(deposit_message)
        else:
            # Get the balance message
            balance_message = get_balance(account_number)
            # Print balance message
            print(balance_message)

    except Exception as e:
        # Handle any exception and print the error message
        print(e)

if __name__ == "__main__":
    chatbot()
