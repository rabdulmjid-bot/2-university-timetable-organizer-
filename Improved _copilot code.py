from datetime import datetime

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]


def read_class_count(day):
    """Read and validate the number of classes for a day."""
    while True:
        try:
            count = int(input("Enter number of classes for {} (0–4): ".format(day)))
            if 0 <= count <= 4:
                return count
        except ValueError:
            pass

        print("Please enter a whole number from 0 to 4.")


def read_time(prompt):
    """Read a valid time in 24-hour HH:MM format."""
    while True:
        time_text = input(prompt).strip()

        try:
            parsed_time = datetime.strptime(time_text, "%H:%M")
            # Ensure the input matches the requested HH:MM format exactly.
            if parsed_time.strftime("%H:%M") == time_text:
                return time_text
        except ValueError:
            pass

        print("Invalid time. Use 24-hour HH:MM format, such as 09:30.")


def to_minutes(time_text):
    """Convert HH:MM into minutes after midnight."""
    hours, minutes = map(int, time_text.split(":"))
    return hours * 60 + minutes


def read_class(class_number):
    """Read and validate one class's code and times."""
    print("\nClass {}".format(class_number))

    # Read a non-empty course code.
    while True:
        code = input("Enter class code: ").strip()
        if code:
            break
        print("Class code cannot be empty.")

    # Read a valid start time once, then retry only the end time as needed.
    start_time = read_time("Enter start time (HH:MM): ")
    start_minutes = to_minutes(start_time)

    while True:
        end_time = read_time("Enter end time (HH:MM): ")
        end_minutes = to_minutes(end_time)

        if end_minutes > start_minutes:
            break
        print("End time must be after start time.")

    return {
        "code": code,
        "start": start_time,
        "end": end_time,
        "start_minutes": start_minutes,
        "end_minutes": end_minutes,
    }


def find_conflicts(day, classes):
    """Return descriptions of all overlapping class pairs for a day."""
    conflicts = []

    for first_index in range(len(classes)):
        for second_index in range(first_index + 1, len(classes)):
            first = classes[first_index]
            second = classes[second_index]

            overlaps = (
                first["start_minutes"] < second["end_minutes"]
                and second["start_minutes"] < first["end_minutes"]
            )

            if overlaps:
                conflicts.append(
                    "{}: {} ({}–{}) overlaps with {} ({}–{})".format(
                        day,
                        first["code"],
                        first["start"],
                        first["end"],
                        second["code"],
                        second["start"],
                        second["end"],
                    )
                )

    return conflicts


def read_day_classes(day):
    """Read all classes for a day and return them with that day's conflicts."""
    print("\n--- {} ---".format(day))
    class_count = read_class_count(day)
    classes = [read_class(number) for number in range(1, class_count + 1)]
    return classes, find_conflicts(day, classes)


def print_timetable(timetable):
    """Print the weekly timetable in aligned columns."""
    print("\n========================")
    print("WEEKLY TIMETABLE")
    print("========================")

    for day in DAYS:
        print("\n{}".format(day))
        print("{:<20} {:<10} {:<10}".format("Course code", "Start", "End"))
        print("{:<20} {:<10} {:<10}".format("-" * 11, "-" * 5, "-" * 3))

        if not timetable[day]:
            print("No classes")
            continue

        for class_info in timetable[day]:
            print(
                "{:<20} {:<10} {:<10}".format(
                    class_info["code"],
                    class_info["start"],
                    class_info["end"],
                )
            )


def print_conflict_report(conflicts):
    """Print the conflict report and total conflict count."""
    print("\n========================")
    print("CONFLICT REPORT")
    print("========================")

    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")

    print("\nTotal number of conflicts: {}".format(len(conflicts)))


def main():
    """Collect the weekly schedule, then display it and its conflicts."""
    timetable = {}
    all_conflicts = []

    # Collect classes and check for conflicts one day at a time.
    for day in DAYS:
        timetable[day], day_conflicts = read_day_classes(day)
        all_conflicts.extend(day_conflicts)

    # Display the completed schedule and conflict report.
    print_timetable(timetable)
    print_conflict_report(all_conflicts)


if __name__ == "__main__":
    main()
