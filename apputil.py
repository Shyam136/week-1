

# add code below ...

import string


def palindrome(word: str) -> bool:
    """
    Return True if the input string is a palindrome, False otherwise.
    Case-insensitive, ignores spaces and punctuation.
    """
    cleaned = "".join(ch.lower() for ch in word if ch.isalnum())
    return cleaned == cleaned[::-1]

git add apputil.py
def parentheses(sequence: str) -> bool:
    """
    Return True if all parentheses in the input string are balanced.
    Balanced means every '(' has a matching ')', in correct order.
    """
    balance = 0
    for ch in sequence:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
            if balance < 0:
                return False
    return balance == 0


# Quick inline tests
if __name__ == "__main__":
    # Palindrome tests
    assert palindrome("racecar") is True
    assert palindrome("Nurses Run") is True
    assert palindrome("Sit on a potato pan, Otis.") is True
    assert palindrome("hello") is False

    # Parentheses tests
    assert parentheses("((blah)()()())") is True
    assert parentheses("(((())blee))") is True
    assert parentheses("(()hello((())()))") is True
    assert parentheses("((((((())") is False
    assert parentheses("()))") is False

    print("All tests passed!")