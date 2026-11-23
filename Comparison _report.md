University Timetable Organizer and Conflict Detector

1. Introduction

Our project is a University Timetable Organizer and Conflict Detector using Python. It helps university students organize their weekly classes and find overlapping class times.

2. Our Original Code

We created our original program using Python functions, loops, and if statements. It uses separate variables to store class information and checks for overlapping class times.

3. Copilot Code

We used GitHub Copilot to generate another version of our program. It uses lists and dictionaries to store class information. It also includes input validation and functions to organize the program. The program checks for overlapping classes and displays a weekly timetable and conflict report.

4. Improved Code

We asked GitHub Copilot to improve its previous code. The improved version organizes the program into separate functions, making it easier to read and understand. It includes input validation, checks that course codes are not empty, and ensures that the end time is after the start time. It also displays the timetable in aligned columns and separates conflict detection from displaying the results.

5. Comparison

* All three programs allow students to enter up to 4 classes per day.
* Our original code uses separate variables to store class information, while both Copilot versions use lists and dictionaries.
* Our original code accepts time as numbers, such as 900, while both Copilot versions use the HH:MM format, such as 09:00.
* The Copilot Code uses the main program directly to collect classes and check conflicts.
* The Improved Copilot Code organizes the program into separate functions, making it easier to read, understand, and maintain.
* The Improved Copilot Code separates timetable input, conflict detection, and displaying results into different functions.
* Both Copilot versions validate class codes and times and check that the end time is after the start time.

6. Conclusion

This project helped us understand Python functions, loops, conditions, lists, dictionaries, and input validation. We also learned how GitHub Copilot can generate and improve code. Comparing the three versions showed us the importance of organizing code, testing programs, and reviewing AI-generated results.

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

Test Conclusion

All three programs successfully detected one conflict between CS101 and MATH101. The test showed that all versions can detect overlapping class times.
