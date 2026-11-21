# University Timetable Organizer and Conflict Detector
# This program asks the student to enter a timetable and reports
# any classes that overlap on the same day.

# Store the allowed days in a list
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

# Store the maximum number of classes allowed per day
MAX_CLASSES = 3


def convert_time_to_minutes(time_text):
    """
    Check whether time_text is a valid 24-hour time.

    Valid format: HH:MM
    Valid examples: 08:30, 12:00, 23:59

    If the time is valid, the function returns its total minutes
    after midnight. If the time is invalid, it returns None.
    """
    # split() separates HH and MM around the colon
    parts = time_text.split(":")

    # A valid time must have exactly two parts
    if len(parts) != 2:
        return None

    hour_text = parts[0]
    minute_text = parts[1]

    # Both parts must contain numbers only
    if not hour_text.isdigit() or not minute_text.isdigit():
        return None

    # Convert the string parts into integers
    hour = int(hour_text)
    minute = int(minute_text)

    # Check the 24-hour time ranges
    if hour < 0 or hour > 23:
        return None

    if minute < 0 or minute > 59:
        return None

    # Convert the time into minutes
    total_minutes = (hour * 60) + minute
    return total_minutes


def format_minutes_as_time(total_minutes):
    """
    Convert minutes after midnight into a HH:MM string.

    Example:
    525 minutes becomes 08:45.
    """
    hour = total_minutes // 60
    minute = total_minutes % 60

    # :02d ensures two digits are displayed
    return f"{hour:02d}:{minute:02d}"


def get_valid_time(prompt):
    """
    Ask the user for a time until a valid HH:MM time is entered.

    The function uses convert_time_to_minutes() to validate the input.
    It returns both the original formatted text and the minute value.
    """
    while True:
        # strip() removes accidental spaces at the beginning or end
        time_text = input(prompt).strip()

        total_minutes = convert_time_to_minutes(time_text)

        if total_minutes is None:
            print("Invalid time. Enter a 24-hour time from 00:00 to 23:59.")
            continue

        return time_text, total_minutes


def get_number_of_classes(day):
    """
    Ask the user for the number of classes on a single day.

    The answer must be a whole number from 0 to MAX_CLASSES.
    """
    while True:
        answer = input(
            f"How many classes do you have on {day}? "
            f"(0-{MAX_CLASSES}): "
        ).strip()

        # isdigit() verifies that the answer contains digits
        if not answer.isdigit():
            print("Invalid input. Enter a whole number.")
            continue

        number = int(answer)

        if number < 0 or number > MAX_CLASSES:
            print(f"Invalid input. Enter a number from 0 to {MAX_CLASSES}.")
            continue

        return number


def get_course_code(class_number, day):
    """
    Ask for and validate a course code.
    """
    while True:
        course_code = input(
            f"Enter course code for class {class_number} on {day}: "
        ).strip()

        if course_code == "":
            print("The course code cannot be empty.")
            continue

        return course_code


def enter_one_class(day, class_number):
    """
    Enter all information for one class.

    The function:
    1. Gets the course code.
    2. Gets a valid start time.
    3. Gets a valid end time.
    4. Makes sure the end time is after the start time.
    """
    course_code = get_course_code(class_number, day)

    # Get a start time in 24-hour format
    start_text, start_minutes = get_valid_time(
        "Enter start time (HH:MM): "
    )

    # Keep asking until the end time is later than the start time
    while True:
        end_text, end_minutes = get_valid_time(
            "Enter end time (HH:MM): "
        )

        if end_minutes <= start_minutes:
            print("Error: End time must be after start time.")
            continue

        break

    # Return a dictionary containing the class information
    return {
        "course_code": course_code,
        "start_text": start_text,
        "start_minutes": start_minutes,
        "end_text": end_text,
        "end_minutes": end_minutes
    }


def enter_timetable():
    """
    Ask the user to enter all classes for Sunday through Thursday.

    The timetable is stored as a dictionary:
    timetable[day] = list of classes
    """
    timetable = {}

    # Repeat once for each day
    for day in DAYS:
        print(f"\n--- {day} ---")

        number_of_classes = get_number_of_classes(day)
        timetable[day] = []

        # Repeat for every class entered for this day
        for class_number in range(1, number_of_classes + 1):
            print(f"\nClass {class_number}:")

            # Add the returned class dictionary to this day
            class_data = enter_one_class(day, class_number)
            timetable[day].append(class_data)

    return timetable


def display_timetable(timetable):
    """
    Display the complete timetable using HH:MM format.
    """
    print("\n========================================")
    print("             DAILY TIMETABLE")
    print("========================================")

    # Loop through each day in its original order
    for day in DAYS:
        print(f"\n{day}:")
        classes = timetable[day]

        if len(classes) == 0:
            print("  No classes")
            continue

        # Loop through each class on the current day
        for course in classes:
            print(
                f"  {course['course_code']}: "
                f"{format_minutes_as_time(course['start_minutes'])} - "
                f"{format_minutes_as_time(course['end_minutes'])}"
            )


def classes_overlap(class_one, class_two):
    """
    Return True when two classes overlap in time.

    A conflict exists when:
    class_one starts before class_two ends
    AND
    class_two starts before class_one ends

    Classes that only touch at a boundary do not conflict.
    Example: 08:00-09:00 and 09:00-10:00 do not conflict.
    """
    return (
        class_one["start_minutes"] < class_two["end_minutes"]
        and
        class_two["start_minutes"] < class_one["end_minutes"]
    )


def detect_conflicts(timetable):
    """
    Compare every pair of classes on the same day.

    Nested loops are used because each class must be compared
    with only the classes that appear after it.
    """
    conflict_report = {}

    for day in DAYS:
        classes = timetable[day]
        daily_conflicts = []

        # i identifies the first class in a pair
        for i in range(len(classes)):
            for j in range(i + 1, len(classes)):
                first_class = classes[i]
                second_class = classes[j]

                if classes_overlap(first_class, second_class):
                    conflict_description = (
                        f"{first_class['course_code']} "
                        f"({format_minutes_as_time(first_class['start_minutes'])}-"
                        f"{format_minutes_as_time(first_class['end_minutes'])}) "
                        f"overlaps with "
                        f"{second_class['course_code']} "
                        f"({format_minutes_as_time(second_class['start_minutes'])}-"
                        f"{format_minutes_as_time(second_class['end_minutes'])})"
                    )

                    daily_conflicts.append(conflict_description)

        # Save this day's conflicts in the report
        conflict_report[day] = daily_conflicts

    return conflict_report


def display_conflict_report(conflict_report):
    """
    Display conflicts for every day and count the total conflicts.

    Each pair of overlapping classes counts as one conflict.
    """
    print("\n========================================")
    print("              CONFLICT REPORT")
    print("========================================")

    total_conflicts = 0

    for day in DAYS:
        print(f"\n{day}:")
        conflicts = conflict_report[day]

        if len(conflicts) == 0:
            print("  No conflicts")
            continue

        # Display and count all conflicts for this day
        for conflict in conflicts:
            print(f"  Conflict: {conflict}")
            total_conflicts += 1

    print("\n----------------------------------------")
    print(f"Total number of conflicts: {total_conflicts}")
    print("----------------------------------------")


def main():
    """
    Run the main parts of the timetable program.
    """
    print("University Timetable Organizer")
    print("==============================")

    timetable = enter_timetable()

    display_timetable(timetable)

    conflict_report = detect_conflicts(timetable)

    display_conflict_report(conflict_report)


# Start the program
main()
