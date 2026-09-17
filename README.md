# QA Automation Technical Task - Python

## Part 1: Algorithmic Tasks
The interactive script for all three tasks is available in `main.py`.

### How to Run:
1. Make sure Python 3 is installed on your machine.
2. Run the script from the command line:
   ```bash
   python main.py
   ```
   ## Part 2: Bracket Sequence Analysis
   Given sequence: [((())()(())]]

1. Can this sequence be considered correct?
Answer: No.

Reasoning:

The bracket sequence starts with an opening square bracket [ but ends with two closing square brackets ]].

The opening and closing bracket counts and types are mismatched/unbalanced.

2. What needs to be changed to make it correct?
Answer:
Change the final closing square bracket ] to a closing parenthesis ).

Original: [((())()(())]]

Corrected: [((())()(()))]

Verification:
The sequence now correctly opens with [, contains a balanced inner group of parentheses ((())()(())), and closes with ].
