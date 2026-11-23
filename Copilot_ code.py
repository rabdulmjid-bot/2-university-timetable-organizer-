def validate_time(time_string):
    """Return time in minutes if HH:MM format is valid, otherwise None."""
    try:
        if len(time_string) != 5 or time_string[2] != ":":
            return None

        hours = int(time_string[:2])
        minutes = int(time_string[3:])
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return hours * 60 + minutes
    except ValueError:
        pass

    return None


def main():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    timetable = {}
    conflict_report = []
    conflict_count = 0

    print("=== Weekly Timetable Program ===")

    for day in days:
        print(f"\n--- {day} ---")

        while True:
            try:
                class_count = int(input("Enter number of classes (0–4): "))
                if 0 <= class_count <= 4:
                    break
                print("Invalid input. Enter a number from 0 to 4.")
            except ValueError:
                print("Invalid input. Enter a number from 0 to 4.")

        classes = []

        for i in range(1, class_count + 1):
            print(f"\nClass {i}:")
            code = input("Enter class code: ").strip()

            while True:
                start_text = input("Enter start time (HH:MM): ").strip()
                start_minutes = validate_time(start_text)

                if start_minutes is None:
                    print("Invalid time format. Use HH:MM (for example, 09:30).")
                    continue

                end_text = input("Enter end time (HH:MM): ").strip()
                end_minutes = validate_time(end_text)

                if end_minutes is None:
                    print("Invalid time format. Use HH:MM (for example, 11:30).")
                    continue

                if end_minutes <= start_minutes:
                    print("End time must be after start time.")
                    continue

                break

            classes.append({
                "code": code,
                "start": start_text,
                "end": end_text,
                "start_minutes": start_minutes,
                "end_minutes": end_minutes
            })

        for i in range(len(classes)):
            for j in range(i + 1, len(classes)):
                first = classes[i]
                second = classes[j]

                overlap = (
                    first["start_minutes"] < second["end_minutes"]
                    and second["start_minutes"] < first["end_minutes"]
                )

                if overlap:
                    conflict_count += 1
                    conflict_report.append(
                        f"{day}: Conflict between {first['code']} "
                        f"({first['start']}–{first['end']}) and "
                        f"{second['code']} "
                        f"({second['start']}–{second['end']})"
                    )

        timetable[day] = classes

    print("\n==============================")
    print("       WEEKLY TIMETABLE")
    print("==============================")

    for day in days:
        print(f"\n{day}:")
        if not timetable[day]:
            print("  No classes")
        else:
            for class_info in timetable[day]:
                print(
                    f"  {class_info['code']} "
                    f"- {class_info['start']} to {class_info['end']}"
                )

    print("\n==============================")
    print("        CONFLICT REPORT")
    print("==============================")

    if not conflict_report:
        print("No conflicts found.")
    else:
        for conflict in conflict_report:
            print(conflict)

    print(f"\nTotal conflicts: {conflict_count}")
    print("\nProgram ended.")


if __name__ == "__main__":
    main()
