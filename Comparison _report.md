University Timetable Organizer and Conflict Detector

1. Introduction

Our project is a University Timetable Organizer and Conflict Detector using Python. It helps university students organize their weekly classes and find overlapping class times.

2. Our Original Code

We created our original program using Python functions, loops, and if statements. It uses separate variables to store class information and checks for overlapping class times.

3. Copilot Code

We used GitHub Copilot to generate another version of our program. It uses lists and dictionaries to store class information. It also includes input validation and functions to organize the program.

4. Improved Code

We asked GitHub Copilot to improve its previous code. The improved version includes more functions, clearer comments, and better input validation. It also checks that course codes are not empty.

5. Comparison

* Our original code allows up to 4 classes per day, while both Copilot versions allow up to 3.
* Our code uses numbers such as 900 to enter time, while Copilot uses HH:MM format, such as 09:00.
* Our original code uses separate variables, while Copilot uses lists and dictionaries.
* The improved code has more organized functions and better input validation.

6. Conclusion

This project helped us understand Python functions, loops, conditions, and input validation. We also learned how GitHub Copilot can help generate and improve code. We learned that AI-generated code should be tested and reviewed.

7. Testing Results

We tested all three versions using the same input data.

Test Scenario

* Day: Sunday
* Course 1: CS101 (09:00–11:00)
* Course 2: MATH101 (10:00–12:00)
* Other days: No classes

Results

1. Our Original Code

* Expected Conflicts: 1
* Actual Result: 1
* Status: Passed

2. Copilot Code

* Expected Conflicts: 1
* Actual Result: 1
* Status: Passed

3. Improved Code

* Expected Conflicts: 1
* Actual Result: 1
* Status: Passed

Conclusion

All three programs successfully detected one conflict between CS101 and MATH101. The test showed that all versions can detect overlapping class times.
