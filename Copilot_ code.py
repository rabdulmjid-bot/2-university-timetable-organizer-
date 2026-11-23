from datetime import datetime

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

weekly_timetable = {}
conflict_report = []
conflict_counter = 0


def time_to_minutes(time_text):
    """Convert HH:MM into minutes after midnight."""
    return int(time_text[:2]) * 60 + int(time_text[3:])


def input_time(prompt):
    while True:
        time_text = input(prompt).strip()

        try:
            parsed_time = datetime.strptime(time_text, "%H:%M")
        except ValueError:
            print("Invalid time format. Use 24-hour HH:MM format.")
            continue

        if parsed_time.hour > 23 or parsed_time.minute > 59:
            print("Invalid time. Enter a time between 00:00 and 23:59.")
            continue

        return time_text


print("Weekly Timetable Program")
print("========================")

for day in DAYS:
    print(f"\n--- {day} ---")

    while True:
        try:
            class_count = int(input(f"Enter number of classes for {day} (0–4): "))
        except ValueError:
            print("Please enter a whole number from 0 to 4.")
            continue

        if 0 <= class_count <= 4:
            break
        print("Number of classes must be from 0 to 4.")

    classes = []

    for class_index in range(1, class_count + 1):
        print(f"\nClass {class_index}")

        while True:
            class_code = input("Enter class code: ").strip()
            if class_code:
                break
            print("Class code cannot be empty.")

        start_time = input_time("Enter start time (HH:MM): ")

        while True:
            end_time = input_time("Enter end time (HH:MM): ")

            start_minutes = time_to_minutes(start_time)
            end_minutes = time_to_minutes(end_time)

            if end_minutes <= start_minutes:
                print("End time must be after start time.")
            else:
                break

        classes.append({
            "code": class_code,
            "start": start_time,
            "end": end_time,
            "start_minutes": start_minutes,
            "end_minutes": end_minutes
        })

    # Check every pair of classes for overlap on this day.
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            first = classes[i]
            second = classes[j]

            overlaps = (
                first["start_minutes"] < second["end_minutes"]
                and second["start_minutes"] < first["end_minutes"]
            )

            if overlaps:
                conflict_counter += 1
                conflict_report.append(
                    f"{day}: {first['code']} ({first['start']}–{first['end']}) "
                    f"overlaps with {second['code']} "
                    f"({second['start']}–{second['end']})"
                )

    weekly_timetable[day] = classes

print("\n========================")
print("WEEKLY TIMETABLE")
print("========================")

for day in DAYS:
    print(f"\n{day}:")

    if not weekly_timetable[day]:
        print("  No classes")
        continue

    for class_info in weekly_timetable[day]:
        print(
            f"  {class_info['code']}: "
            f"{class_info['start']}–{class_info['end']}"
        )

print("\n========================")
print("CONFLICT REPORT")
print("========================")

if conflict_report:
    for conflict in conflict_report:
        print(conflict)
else:
    print("No conflicts found.")

print(f"\nTotal number of conflicts: {conflict_counter}")
