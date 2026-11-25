"""
Quiz Application - Programming Fundamentals and Logic Building Using Python
Name: Dhiraj Kumar | ERP No.: RU-26-02018
"""

import random

PASS_PERCENTAGE = 50

# Question bank: list of dictionaries (question, options, answer)
QUESTIONS = [
    # --- Fixed test questions (always asked first, in this order) ---
    {"question": "Keyword to define a function?",
     "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
     "answer": "B"},
    {"question": 'len("Hi") = ?',
     "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
     "answer": "B"},
    {"question": "Mutable type?",
     "options": {"A": "tuple", "B": "str", "C": "list", "D": "int"},
     "answer": "C"},
    # --- Random pool ---
    {"question": "Which symbol starts a comment in Python?",
     "options": {"A": "//", "B": "#", "C": "/*", "D": "--"},
     "answer": "B"},
    {"question": "Which function prints output to the console?",
     "options": {"A": "echo()", "B": "show()", "C": "print()", "D": "write()"},
     "answer": "C"},
    {"question": "What is the type of 3.14?",
     "options": {"A": "int", "B": "float", "C": "str", "D": "bool"},
     "answer": "B"},
    {"question": "Which loop runs while a condition is True?",
     "options": {"A": "for", "B": "do", "C": "while", "D": "repeat"},
     "answer": "C"},
    {"question": "How do you start a list?",
     "options": {"A": "()", "B": "[]", "C": "{}", "D": "<>"},
     "answer": "B"},
    {"question": "Which method adds an item to the end of a list?",
     "options": {"A": "add()", "B": "push()", "C": "append()", "D": "insert_end()"},
     "answer": "C"},
    {"question": "What does 7 // 2 give?",
     "options": {"A": "3.5", "B": "3", "C": "4", "D": "1"},
     "answer": "B"},
]

NUM_FIXED = 3  # first 3 questions are fixed for testing
NUM_RANDOM = 2  # TODO: decide how many extra random questions to ask


def ask(q):
    """Show one question. Keep asking until a valid option (A-D) is given.
    Return True if correct, False if wrong."""
    # TODO 1: print q["question"] and each option (A, B, C, D)
    # TODO 2: use a while True loop to read input
    #         Hint: .strip().upper() cleans the input
    # TODO 3: if input is not in "ABCD", print
    #         "Invalid option. Enter A, B, C or D."  and ask AGAIN (Test Case 3)
    # TODO 4: if valid, compare with q["answer"]; if wrong print
    #         "Q<n> Wrong. Correct answer: X"  (Test Case 4)
    #         if right print "Correct!"
    pass


def build_quiz():
    """Return the list of questions to ask: fixed ones first, then random ones."""
    # TODO 5: fixed = QUESTIONS[:NUM_FIXED]
    #         pool = QUESTIONS[NUM_FIXED:]
    #         extra = random.sample(pool, NUM_RANDOM)
    #         return fixed + extra
    pass


def show_result(score, total, wrong_answers):
    """Print score, percentage and pass/fail."""
    # TODO 6: percentage = score / total * 100
    # TODO 7: print  Score: x/y | Percentage: z.zz%   (use :.2f)
    # TODO 8: print Result: Pass if percentage >= PASS_PERCENTAGE else Fail
    # TODO 9: if Fail, also print "Correct answers: B, B, C"
    pass


def main():
    print("=== Quiz Application ===")
    quiz = build_quiz()
    score = 0
    correct_answers = []
    # TODO 10: loop over quiz, call ask(), add 1 to score when True,
    #          and store each q["answer"] in correct_answers
    # TODO 11: call show_result(...)


if __name__ == "__main__":
    main()
