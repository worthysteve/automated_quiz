# automated_quiz

This project is an automated, console-based multiple-choice quiz titled "HOW SMART ARE YOU", created as a final submission for the Code In Place program. The quiz presents a diverse set of 100 questions drawn from categories including:

- Science
- Arts
- Mathematics
- Computer Science
- Machine Learning
- Artificial Intelligence
- Deep Learning
- Current Affairs
- General Knowledge

Each question offers four answer options (A, B, C, D), from which the user must select the correct one.

## ✅ Scoring Rules:

- Questions are grouped in batches of 10.
  - Batch 1: 1 point per correct answer
  - Batch 2: 2 points per correct answer
  - Batch 3: 3 points per correct answer
  - ... and so on.
- Users retain their score if the answer is wrong (no negative marking).

The game ends when:
- The user gets 10 answers wrong, or
- The user types "exit" or "q" to quit early, or
- All questions are exhausted.

At the end of the quiz, the system prints the user's final score out of the maximum possible score (based on the total number of questions).
