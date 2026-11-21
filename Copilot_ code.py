# University Timetable Organizer and Conflict Detector
# Beginner-friendly Python program

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]


def validate_time(time_text):
    """
    Validate a time in 24-hour HH:MM format.

    Returns the time as minutes after midnight if valid.
    Returns None if the time is invalid.
    """
    # Time must contain exactly one colon
    if ":" not in time_text:
        return None

    parts = time_text.split(":")

    # Time must have exactly two parts
    if len(parts) != 2:
        return None

    hour_text = parts[0]
    minute_text = parts[1]

    # Both parts must contain numbers
    if not hour_text.isdigit() or not minute_text.isdigit():
        return None

    hour = int(hour_text)
    minute = int(minute_text)

    # 24-hour format valid range: 00:00 to 23:59
    if hour < 0 or hour > 23:
        return None

    if minute < 0 or minute > 59:
        return None

    # Convert the time to minutes
    time_in_minutes = (hour * 60) + minute
    return time_in_minutes


def input_time(prompt):
    """
    Keep asking the user until a valid 24-hour time is entered.
    """
    while True:
        time_text = input(prompt).strip()

        time_in_minutes = validate_time(time_text)

        if time_in_minutes is None:
            print("Invalid time! Please use HH:MM in 24-hour format.")
        else:
            return time_text, time_in_minutes


def format_time(time_in_minutes):
    """
    Convert minutes after midnight into HH:MM format.
    """
    hours = time_in_minutes // 60
    minutes = time_in_minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def enter_number_of_classes(day):
    """
    Ask the user how many classes they have on a specific day.
    """
    while True:
        number_text = input(f"\nHow many classes do you have on {day}? (0-3): ")

        if not number_text.isdigit():
            print("Please enter a whole number from 0 to 3.")
            continue

        number = int(number_text)

        if number < 0 or number > 3:
            print("You can enter from 0 to 3 classes per day.")
        else:
            return number


def enter_timetable():
    """
    Enter the timetable for Sunday through Thursday.
    """
    timetable = {}

    for day in DAYS:
        number_of_classes = enter_number_of_classes(day)
        timetable[day] = []

        for class_number in range(1, number_of_classes + 1):
            print(f"\n--- {day}: Class {class_number} ---")

            course_code = input("Enter course code: ").strip()

            # Course code is allowed to be empty, but adding a default is useful
            if course_code == "":
                course_code = "UNNAMED"

            start_text, start_minutes = input_time(
                "Enter start time (HH:MM): "
            )

            while True:
                end_text, end_minutes = input_time(
                    "Enter end time (HH:MM): "
                )

                if end_minutes <= start_minutes:
                    print("End time must be after start time.")
                else:
                    break

            timetable[day].append({
                "course_code": course_code,
                "start_text": start_text,
                "start_minutes": start_minutes,
                "end_text": end_text,
                "end_minutes": end_minutes
            })

    return timetable


def display_timetable(timetable):
    """
    Display all classes in timetable order as entered.
    """
    print("\n========================================")
    print("             DAILY TIMETABLE")
    print("========================================")

    for day in DAYS:
        print(f"\n{day}:")

        if len(timetable[day]) == 0:
            print("  No classes")
            continue

        for course in timetable[day]:
            print(
                f"  {course['course_code']}: "
                f"{format_time(course['start_minutes'])} - "
                f"{format_time(course['end_minutes'])}"
            )


def times_overlap(start1, end1, start2, end2):
    """
    Return True if two time periods overlap.

    Two classes do not conflict if one ends exactly when
    the other begins.
    """
    return start1 < end2 and start2 < end1


def detect_conflicts(timetable):
    """
    Detect conflicts between every pair of classes on the same day.
    """
    conflict_report = {}

    for day in DAYS:
        classes = timetable[day]
        day_conflicts = []

        # Compare each pair of classes
        for i in range(len(classes)):
            for j in range(i + 1, len(classes)):
                first = classes[i]
                second = classes[j]

                if times_overlap(
                    first["start_minutes"],
                    first["end_minutes"],
                    second["start_minutes"],
                    second["end_minutes"]
                ):
                    conflict = (
                        f"{first['course_code']} "
                        f"({format_time(first['start_minutes'])}-"
                        f"{format_time(first['end_minutes'])}) conflicts with "
                        f"{second['course_code']} "
                        f"({format_time(second['start_minutes'])}-"
                        f"{format_time(second['end_minutes'])})"
                    )
                    day_conflicts.append(conflict)

        conflict_report[day] = day_conflicts

    return conflict_report


def display_conflict_report(conflict_report):
    """
    Display conflicts and the total number of conflicts.
    """
    print("\n========================================")
    print("              CONFLICT REPORT")
    print("========================================")

    total_conflicts = 0

    for day in DAYS:
        conflicts = conflict_report[day]

        print(f"\n{day}:")

        if len(conflicts) == 0:
            print("  No conflicts")
        else:
            for conflict in conflicts:
                print(f"  Conflict: {conflict}")
                total_conflicts += 1

    print("\n----------------------------------------")
    print(f"Total number of conflicts: {total_conflicts}")
    print("----------------------------------------")


def main():
    print("University Timetable Organizer")
    print("==============================")

    timetable = enter_timetable()
    display_timetable(timetable)

    conflict_report = detect_conflicts(timetable)
    display_conflict_report(conflict_report)


main()
