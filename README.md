# 🎓 Student Grade Calculator

## 📌 Project Overview
A comprehensive grade calculator that processes multiple students' marks, calculates grades with personalized comments, and provides class statistics. This project is a robust, purely Python-based command-line interface (CLI) application developed to streamline the grading process for educators while demonstrating strong foundational programming skills.

## 🚀 Setup Instructions (How to Run)
**Prerequisites:** Python 3.x installed on your system. No external libraries required.

```bash
# 1. Clone the repository and navigate to the project folder
git clone https://github.com/rutujakharode6-max/STUDENT-GRADE-CALCULATOR.git
cd week2-grade-calculator

# 2. Run the program interactively
python grade_calculator.py

# 3. Alternatively, run a sample test with provided dummy data
python grade_calculator.py < test_students.txt
```

## 📂 Code Structure
The repository is well-organized with a clear file hierarchy:
```text
week2-grade-calculator/
│── grade_calculator.py    # Main application containing all logic and menus
│── test_students.txt      # Dummy input data for automated testing
│── results_sample.txt     # Example of the exported text report
│── README.md              # Comprehensive project documentation
└── .gitignore             # Git ignore file for Python cache and local reports
```

## ✨ Features
- [x] **Processes multiple students**: Handles any number of students in a single session.
- [x] **Calculates grades based on custom grading system**: Accurately maps numerical averages to letter grades.
- [x] **Provides personalized comments for each student**: Generates dynamic feedback based on performance.
- [x] **Calculates class statistics**: Automatically computes the class average, highest score, and lowest score.
- [x] **Formatted table output with color coding**: Utilizes ANSI escape codes for a visually appealing terminal display.
- [x] **Input validation for all user inputs**: Prevents crashes from empty strings or non-integer inputs.
- [x] **Error handling for edge cases**: Strict `try-except` blocks protect against unexpected user behavior.
- [x] **Search functionality for specific students**: Allows case-insensitive, partial-match searching of the database.
- [x] **Save results to file option**: Exports timestamped `.txt` reports containing all data and statistics.

## 🧠 Technical Details & What I Learned
During the development of this project, several core algorithms and data structures were heavily utilized:
- **Conditional Logic**: Using `if/elif/else` for decision making when mapping numerical boundaries to specific letter grades and comments.
- **Lists & Dictionaries**: Storing and manipulating collections of data. Each student's data is housed in a dictionary, which is then appended to a master `comprehensive_results` list for easy iteration and retrieval.
- **Loops**: Using `for` and `while` loops for repetition. The application utilizes a persistent `while True` loop for the main menu, and nested loops for gathering individual subject marks.
- **Error Handling**: Using `try-except` blocks wrapped inside `while` loops to infinitely prompt the user until valid numerical data is entered, preventing fatal crashes (e.g., `ValueError`).
- **Functions**: Organizing code into reusable, modular blocks (`calculate_grade()`, `get_grade_comment()`, `main_menu()`).
- **List Comprehensions**: Used advanced Python list comprehensions to efficiently extract data for statistical analysis (e.g., `[res['average'] for res in comprehensive_results]`).

## 💡 Challenges & Solutions

**Challenge 1: Handling invalid marks input**
- **Solution**: Used an infinite `while True` loop combined with a `try-except` block. If a user inputs text instead of a number, the `ValueError` is caught, an error message is displayed, and the loop restarts, asking for input again without crashing the program.

**Challenge 2: Formatting the results table**
- **Solution**: Implemented Python's string formatting with fixed widths (e.g., `<15` for left-aligning names, `>9` for right-aligning numbers). Also dynamically injected ANSI color codes (Green for A, Red for F) into the f-strings for a premium CLI experience.

**Challenge 3: Calculating multiple statistics**
- **Solution**: Extracted all averages using list comprehensions and passed them through built-in Python math functions (`max()`, `min()`, `sum()`) to efficiently calculate the highest, lowest, and class-wide averages.

## 📊 Grading System & Testing Evidence

**Grading System:**
- **A**: 90-100 (Excellent!)
- **B**: 80-89 (Very Good!)
- **C**: 70-79 (Good)
- **D**: 60-69 (Needs Improvement)
- **F**: 0-59 (Failed - Please seek help)

**Testing Evidence & Validation:**
The application was rigorously tested with edge cases:
- *Test Case 1 (Out of bounds)*: Entering `105` for a mark triggers the bounds validation and rejects the input.
- *Test Case 2 (String instead of Int)*: Entering `"Eighty"` for a mark triggers the `ValueError` exception block.
- *Test Case 3 (Empty Name)*: Hitting 'Enter' without typing a name triggers the `.strip()` validation loop.

## 📸 Visual Documentation (Sample Output)

```text
===========================================
      STUDENT GRADE CALCULATOR
===========================================

Number of students: 3

=== STUDENT 1 ===
Name: John Smith
Math: 85
Science: 92
English: 88

=== STUDENT 2 ===
Name: Sarah Johnson
Math: 78
Science: 81
English: 85

===========================================
            RESULTS SUMMARY
===========================================
Name           | Avg | Grade | Comment
---------------+-----+-------+-----------------
John Smith     | 88.3|   B   | Very Good!
Sarah Johnson  | 81.3|   B   | Very Good!

===========================================
          CLASS STATISTICS
===========================================
Total Students: 2
Class Average: 84.8
Highest Average: 88.3 (John Smith)
Highest Average Student: John Smith
Lowest Average: 81.3 (Sarah Johnson)
Lowest Average Student: Sarah Johnson
```

---
*Developed for the Developers Arena Internship.*
