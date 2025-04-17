"""
LeetCode-style Problem: Process and Summarize Transactions (Medium)

You are given a file named "data.txt" that contains transaction records. Each line in the file 
follows the format:

<user_id>,<amount>

- `user_id`: a string identifier for the user (e.g., "user123")
- `amount`: a floating-point number that may be positive (credit) or negative (debit)

Your task is to implement the function `summarize_transactions(input_file, output_file)` that:

1. Reads the `input_file` line by line.
2. Accumulates the total balance for each user.
3. Writes the result to the `output_file`, where each line is:
   <user_id>,<net_balance>

   The result should be sorted by `user_id` in ascending order.
   Balances should be rounded to 2 decimal places.

Example Input File: data.txt
----------------------------
user1,100.0
user2,-50.5
user1,-25.0
user3,10.0
user2,20.0

Expected Output File Content:
-----------------------------
user1,75.00
user2,-30.50
user3,10.00

Constraints:
------------
- You may assume the input file fits in memory.
- Invalid lines (e.g., missing fields, malformed floats) should be ignored.
- An output file should be created even if all input lines are invalid.

Function Signature:
-------------------
def summarize_transactions(input_file: str, output_file: str) -> None:
"""

def summarize_transactions(input_file: str, output_file: str) -> None:
    user_balances = {}
    with open ("~/Desktop/data.txt", "r") as f:
        for line in f:
            user, amount = line.split(",")
            if user  in user_balances:
                user_balances[user] += float(amount)
            else:
                user_balances[user] = float(amount)
    with open ("~/Desktop/dataUpdated.txt", "w") as f:
        for user, balance in user_balances.items():
            f.write(user + ","+ str(balance)+ "\n")
            



# Test Cases
import os

def test_summarize_transactions():
    test_input = "test_data.txt"
    test_output = "test_output.txt"

    with open(test_input, "w") as f:
        f.write(
            "user1,100.0\n"
            "user2,-50.5\n"
            "user1,-25.0\n"
            "user3,10.0\n"
            "user2,20.0\n"
            "user4,notanumber\n"
            "malformedline\n"
        )

    summarize_transactions(test_input, test_output)

    with open(test_output, "r") as f:
        result = f.read().strip().split("\n")

    expected = [
        "user1,75.00",
        "user2,-30.50",
        "user3,10.00"
    ]

    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"

    os.remove(test_input)
    os.remove(test_output)

if __name__ == "__main__":
    test_summarize_transactions()
    print("All test cases passed.")
