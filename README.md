# Quiz Application

A console-based multiple-choice quiz written in Python 3. It asks questions randomly from a question bank, checks each answer, keeps the score and shows the final result.

**Student:** Dhiraj Kumar | **ERP No.:** RU-26-02018
**Program:** B.Tech CSE, First Semester, Section L
**Course:** Programming Fundamentals and Logic Building Using Python (RU-100-01-0021)
**Mentor:** Rishabh Vishwakarma
**University:** Rungta International Skills University, Bhilai

## Features

- Question bank stored as a list of dictionaries (question, options, answer), with 10+ questions
- Random question selection using the `random` module
- The first three questions are fixed (for testing); the rest are random
- Input validation: an invalid option shows a message and asks the same question again
- Final score, percentage (2 decimals) and Pass/Fail message (pass mark 50%)
- Correct answers are shown when the result is Fail

## Concepts Used

Lists, dictionaries, loops, conditionals, functions, `random` module.

## Requirements

- Python 3.10 or later
- No external libraries (only the standard library)

## How to Run

```bash
python quiz_app.py
```

Type A, B, C or D for each question and press Enter.

## Project Structure

```
quiz-application/
├── quiz_app.py        # main program
├── README.md          # this file
└── screenshots/       # terminal screenshots of the test cases
```

## Functions

| Function | Purpose |
|---|---|
| `build_quiz()` | Returns the fixed questions followed by random ones |
| `ask(q, number)` | Shows one question, validates input, returns True or False |
| `show_result(score, total, correct_answers)` | Prints score, percentage and Pass/Fail |
| `main()` | Runs the quiz loop and keeps the score |

## Test Cases

| # | Case | Input | Expected Output |
|---|---|---|---|
| 1 | Normal input | B, B, C | Score: 3/3, Percentage: 100.00%, Result: Pass |
| 2 | Boundary / minimum input | A, A, A | Score: 0/3, Percentage: 0.00%, Result: Fail, Correct answers: B, B, C |
| 3 | Invalid input | Q1: E, then B | Invalid option. Enter A, B, C or D. Q1 is asked again, then Correct! |
| 4 | Different valid scenario | B, A, C | Q2 Wrong. Correct answer: B, Score: 2/3, Percentage: 66.67%, Result: Pass |

## Screenshots

<!-- Add your own screenshots after running each test case -->

| Test Case 1 | Test Case 2 |
|---|---|
| ![Test Case 1](screenshots/test_case_1.png) | ![Test Case 2](screenshots/test_case_2.png) |

| Test Case 3 | Test Case 4 |
|---|---|
| ![Test Case 3](screenshots/test_case_3.png) | ![Test Case 4](screenshots/test_case_4.png) |

## Future Improvements

- Timer for each question
- Question categories and difficulty levels
- Saving high scores to a file

## Author

Dhiraj Kumar, B.Tech CSE, Rungta International Skills University
