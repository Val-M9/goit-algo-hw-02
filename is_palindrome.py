from collections import deque


def is_palindrome(text):
    letters = deque(''.join(text.lower().split()))
    while len(letters) > 1:
        if letters.popleft() != letters.pop():
            return f'"{text}" is not a palindrome'
        else:
            return f'"{text}" is a palindrome'


print(is_palindrome("Pan Level nap"))
