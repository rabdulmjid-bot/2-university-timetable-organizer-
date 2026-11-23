# ============================================
# University Timetable Organizer and Conflict Detector
# ============================================

def get_day_name(day_number):
    # Section: Get the day name
    if day_number == 1:
        return "Sunday"
    elif day_number == 2:
        return "Monday"
    elif day_number == 3:
        return "Tuesday"
    elif day_number == 4:
        return "Wednesday"
    else:
        return "Thursday"


def to_minutes(time_number):
    # Section: Convert a 24-hour integer into minutes
    time_text = str(time_number)

    if len(time_text) <= 2:
        hour = int(time_text)
        minute = 0
    elif len(time_text) == 3:
        hour = int(time_text[0])
        minute = int(time_text[1:3])
    else:
        hour = int(time_text[:-2])
        minute = int(time_text[-2:])

    return hour * 60 + minute


def read_time(message):
    # Section: Read and validate a time
    while True:
        time_text = input(message).strip()

        try:
            time_number = int(time_text)
        except ValueError:
            print("Invalid time. Enter a number such as 830 or 1330.")
            continue

        if time_number < 0:
            print("Time cannot be negative.")
            continue

        if len(time_text) == 1 or len(time_text) == 2:
            hour = int(time_text)
            minute = 0
        elif len(time_text) == 3:
            hour = int(time_text[0])
            minute = int(time_text[1:3])
        else:
            hour = int(time_text[:-2])
            minute = int(time_text[-2:])

        if hour > 23:
            print("Hour must be between 0 and 23.")
            continue

        if minute > 59:
            print("Minutes must be between 0 and 59.")
            continue

        return time_number


def read_end_time(message, start_time):
    # Section: Read and validate the end time
    while True:
        end_time = read_time(message)
        start_minutes = to_minutes(start_time)
        end_minutes = to_minutes(end_time)

        if end_minutes <= start_minutes:
            print("End time must be after start time.")
            continue

        return end_time


def to_time(time_number):
    # Section: Format a time as HH:MM
    time_text = str(time_number)

    if len(time_text) <= 2:
        hour = int(time_text)
        minute = 0
    elif len(time_text) == 3:
        hour = int(time_text[0])
        minute = int(time_text[1:3])
    else:
        hour = int(time_text[:-2])
        minute = int(time_text[-2:])

    return str(hour).zfill(2) + ":" + str(minute).zfill(2)


def has_conflict(start1, end1, start2, end2):
    # Section: Check whether two classes overlap
    start1_minutes = to_minutes(start1)
    end1_minutes = to_minutes(end1)
    start2_minutes = to_minutes(start2)
    end2_minutes = to_minutes(end2)

    if start1_minutes < end2_minutes and start2_minutes < end1_minutes:
        return True
    return False


def make_line(course_code, start_time, end_time):
    # Section: Create a timetable line
    return course_code + " " + to_time(start_time) + " - " + to_time(end_time)


# Section: Initialize weekly timetable strings
# Strings and "|" separators are used instead of lists/dictionaries.
sunday_codes = ""
sunday_starts = ""
sunday_ends = ""

monday_codes = ""
monday_starts = ""
monday_ends = ""

tuesday_codes = ""
tuesday_starts = ""
tuesday_ends = ""

wednesday_codes = ""
wednesday_starts = ""
wednesday_ends = ""

thursday_codes = ""
thursday_starts = ""
thursday_ends = ""

# Section: Initialize the conflict report
conflict_report = ""
total_conflicts = 0

print("University Timetable Organizer and Conflict Detector")
print()

# Section: Enter data for each day
for day_number in range(1, 6):
    day_name = get_day_name(day_number)
    print("\n" + day_name)

    # Section: Read a valid class count
    while True:
        try:
            number_of_classes = int(input("Enter number of classes (0-4): "))
        except ValueError:
            print("Invalid input. Enter a number from 0 to 4.")
            continue

        if number_of_classes < 0 or number_of_classes > 4:
            print("Invalid input. Enter a number from 0 to 4.")
        else:
            break

    day_codes = ""
    day_starts = ""
    day_ends = ""

    # Section: Read classes for the day
    for class_number in range(1, number_of_classes + 1):
        course_code = input(
            "Enter course code for class " + str(class_number) + ": "
        ).strip()

        if course_code == "":
            print("Course code cannot be empty.")
            class_number = class_number - 1
            continue

        start_time = read_time(
            "Enter start time for " + course_code +
            " (for example, 830 or 1330): "
        )
        end_time = read_end_time(
            "Enter end time for " + course_code +
            " (for example, 930 or 1430): ",
            start_time
        )

        if day_codes == "":
            day_codes = course_code
            day_starts = str(start_time)
            day_ends = str(end_time)
        else:
            day_codes = day_codes + "|" + course_code
            day_starts = day_starts + "|" + str(start_time)
            day_ends = day_ends + "|" + str(end_time)

    # Section: Store the entered day
    if day_number == 1:
        sunday_codes = day_codes
        sunday_starts = day_starts
        sunday_ends = day_ends
    elif day_number == 2:
        monday_codes = day_codes
        monday_starts = day_starts
        monday_ends = day_ends
    elif day_number == 3:
        tuesday_codes = day_codes
        tuesday_starts = day_starts
        tuesday_ends = day_ends
    elif day_number == 4:
        wednesday_codes = day_codes
        wednesday_starts = day_starts
        wednesday_ends = day_ends
    else:
        thursday_codes = day_codes
        thursday_starts = day_starts
        thursday_ends = day_ends

# Section: Detect conflicts for all days
for day_number in range(1, 6):
    day_name = get_day_name(day_number)

    if day_number == 1:
        day_codes = sunday_codes
        day_starts = sunday_starts
        day_ends = sunday_ends
    elif day_number == 2:
        day_codes = monday_codes
        day_starts = monday_starts
        day_ends = monday_ends
    elif day_number == 3:
        day_codes = tuesday_codes
        day_starts = tuesday_starts
        day_ends = tuesday_ends
    elif day_number == 4:
        day_codes = wednesday_codes
        day_starts = wednesday_starts
        day_ends = wednesday_ends
    else:
        day_codes = thursday_codes
        day_starts = thursday_starts
        day_ends = thursday_ends

    if day_codes == "":
        continue

    codes = day_codes.split("|")
    starts = day_starts.split("|")
    ends = day_ends.split("|")

    # Section: Compare every pair of classes
    for first_index in range(len(codes)):
        for second_index in range(first_index + 1, len(codes)):
            conflict = has_conflict(
                int(starts[first_index]),
                int(ends[first_index]),
                int(starts[second_index]),
                int(ends[second_index])
            )

            if conflict:
                total_conflicts = total_conflicts + 1
                conflict_report = conflict_report + (
                    day_name + ": " +
                    codes[first_index] + " conflicts with " +
                    codes[second_index] + "\n"
                )

# Section: Display the weekly timetable
print("\n==============================")
print("Weekly Timetable")
print("==============================")

for day_number in range(1, 6):
    day_name = get_day_name(day_number)

    if day_number == 1:
        day_codes = sunday_codes
        day_starts = sunday_starts
        day_ends = sunday_ends
    elif day_number == 2:
        day_codes = monday_codes
        day_starts = monday_starts
        day_ends = monday_ends
    elif day_number == 3:
        day_codes = tuesday_codes
        day_starts = tuesday_starts
        day_ends = tuesday_ends
    elif day_number == 4:
        day_codes = wednesday_codes
        day_starts = wednesday_starts
        day_ends = wednesday_ends
    else:
        day_codes = thursday_codes
        day_starts = thursday_starts
        day_ends = thursday_ends

    print("\n" + day_name + ":")

    if day_codes == "":
        print("  No classes")
        continue

    codes = day_codes.split("|")
    starts = day_starts.split("|")
    ends = day_ends.split("|")

    # Section: Mark each class involved in a conflict
    for class_index in range(len(codes)):
        timetable_line = make_line(
            codes[class_index],
            int(starts[class_index]),
            int(ends[class_index])
        )

        involved_in_conflict = False

        for other_index in range(len(codes)):
            if class_index != other_index:
                conflict = has_conflict(
                    int(starts[class_index]),
                    int(ends[class_index]),
                    int(starts[other_index]),
                    int(ends[other_index])
                )

                if conflict:
                    involved_in_conflict = True

        if involved_in_conflict:
            timetable_line = timetable_line + " <-- CONFLICT!"

        print("  " + timetable_line)

# Section: Display the conflict report
print("\n==============================")
print("Conflict Report")
print("==============================")

if total_conflicts == 0:
    print("No conflicts found")
else:
    print(conflict_report, end="")
    print("Total number of conflicts: " + str(total_conflicts))

print("\nProgram ended.")
