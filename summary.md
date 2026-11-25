# Project Summary: Quiz Application

**Student:** Dhiraj Kumar (RU-26-02018)
**Course:** Programming Fundamentals and Logic Building Using Python (RU-100-01-0021)
**Mentor:** Rishabh Vishwakarma
**Allocated:** 14 October 2026 | **Submission:** 16 November 2026

## Overview

A console-based quiz in Python 3 that asks multiple-choice questions randomly from a question bank, checks each answer, keeps the score and displays the result.

## Problem

Conducting a quiz by hand means asking questions, checking answers and counting marks manually. This program does all three automatically and gives an instant Pass or Fail result (pass mark 50%).

## Approach

1. Store 10+ questions as a list of dictionaries (question, options, answer).
2. Ask the 3 fixed test questions first, then random questions using `random.sample()`.
3. Read each answer in a loop; an invalid option repeats the same question.
4. Add 1 to the score for each correct answer.
5. Show score, percentage (2 decimals) and Pass or Fail; on Fail, also show the correct answers.

## Concepts and Tools

Python 3, lists, dictionaries, loops, conditionals, functions, `random` module.

## Functions

| Function | Role |
|---|---|
| `build_quiz()` | Builds the list of questions to ask |
| `ask(q, number)` | Asks one question, validates input, returns True or False |
| `show_result(...)` | Prints score, percentage and Pass or Fail |
| `main()` | Runs the quiz and keeps the score |

## Test Cases

| # | Input | Expected Output |
|---|---|---|
| 1 | B, B, C | 3/3, 100.00%, Pass |
| 2 | A, A, A | 0/3, 0.00%, Fail, correct answers B, B, C |
| 3 | Q1: E, then B | Invalid option message, Q1 asked again, Correct! |
| 4 | B, A, C | Q2 wrong (correct: B), 2/3, 66.67%, Pass |

## Deliverables

| Item | File | Status |
|---|---|---|
| Code | `quiz_app.py` | [update: in progress / done] |
| Report | `Quiz_Application_Project_Report.docx` | [update] |
| PPT | `Quiz_Application_PPT.pptx` | [update] |
| Abstract | `Abstract_Quiz_Application_Shaastrarth_2026.docx` | [update] |
| README | `README.md` | Ready |
| Test screenshots | `screenshots/` | [update after running all 4 cases] |
| GitHub link | | [add after upload] |

## Key Learnings

- Structuring data with lists and dictionaries
- Input validation with loops
- Breaking a program into functions
- Testing against expected outputs

## Future Scope

Timer, question categories, difficulty levels, saving high scores.
