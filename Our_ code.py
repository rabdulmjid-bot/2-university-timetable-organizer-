def get_day_name(number):
    if number == 1:
        return "SUNDAY"
    elif number == 2:
        return "MONDAY"
    elif number == 3:
        return "TUESDAY"
    elif number == 4:
        return "WEDNESDAY"
    else:
        return "THURSDAY"

def read_time(prompt):
    while True:
        value = int(input(prompt))
        hours = value // 100
        minutes = value % 100
        if value >= 0 and hours <= 23 and minutes <= 59:
            break
        print("Invalid time! Please use 24-hour format (830 , 1330..):")
    return hours * 60 + minutes

def read_end_time(start):
    while True:
        end = read_time("End time (In 24h format): ")
        if end > start:
            break
        print("End time must be after start time! Please try again:")
    return end

def to_time(total):
    hours = total // 60
    minutes = total % 60
    result = ""
    if hours < 10:
        result = "0"
    result = result + str(hours) + ":"
    if minutes < 10:
        result = result + "0"
    result = result + str(minutes)
    return result

def has_conflict(start1, end1, start2, end2):
    return start1 < end2 and start2 < end1

def make_line(code, start, end, conflict):
    line = "   " + code + "  " + to_time(start) + " - " + to_time(end)
    if conflict == True:
        line = line + "   <-- CONFLICT!"
    return line + "\n"

week_report = ""
conflict_report = ""
conflict_count = 0

for day_number in range(1, 6):
    day = get_day_name(day_number)
    print("\n " + day + " ")

    count = int(input("Number of classes on this day (0-4): "))
    while count < 0 or count > 4:
        count = int(input("The limit for th number of classes per2 day is 0-4! Please try again: "))

    code1 = ""
    start1 = 0
    end1 = 0
    code2 = ""
    start2 = 0
    end2 = 0
    code3 = ""
    start3 = 0
    end3 = 0
    code4 = ""
    start4 = 0
    end4 = 0

    if count >= 1:
        print("Class 1")
        code1 = input("Course code: ")
        start1 = read_time("Start time (In 24h format): ")
        end1 = read_end_time(start1)
    if count >= 2:
        print("Class 2")
        code2 = input("Course code: ")
        start2 = read_time("Start time (In 24h format): ")
        end2 = read_end_time(start2)
    if count >= 3:
        print("Class 3")
        code3 = input("Course code: ")
        start3 = read_time("Start time (In 24h format): ")
        end3 = read_end_time(start3)
    if count >= 4:
        print("Class 4")
        code4 = input("Course code: ")
        start4 = read_time("Start time (In 24h format): ")
        end4 = read_end_time(start4)

    conflict12 = False
    conflict13 = False
    conflict14 = False
    conflict23 = False
    conflict24 = False
    conflict34 = False

    if count >= 2 and has_conflict(start1, end1, start2, end2):
        conflict12 = True
        conflict_report = conflict_report + day + ": " + code1 + " and " + code2 + "\n"
        conflict_count += 1
    if count >= 3 and has_conflict(start1, end1, start3, end3):
        conflict13 = True
        conflict_report = conflict_report + day + ": " + code1 + " and " + code3 + "\n"
        conflict_count += 1
    if count >= 4 and has_conflict(start1, end1, start4, end4):
        conflict14 = True
        conflict_report = conflict_report + day + ": " + code1 + " and " + code4 + "\n"
        conflict_count += 1
    if count >= 3 and has_conflict(start2, end2, start3, end3):
        conflict23 = True
        conflict_report = conflict_report + day + ": " + code2 + " and " + code3 + "\n"
        conflict_count += 1
    if count >= 4 and has_conflict(start2, end2, start4, end4):
        conflict24 = True
        conflict_report = conflict_report + day + ": " + code2 + " and " + code4 + "\n"
        conflict_count += 1
    if count >= 4 and has_conflict(start3, end3, start4, end4):
        conflict34 = True
        conflict_report = conflict_report + day + ": " + code3 + " and " + code4 + "\n"
        conflict_count += 1

    week_report = week_report + day + ":\n"
    if count == 0:
        week_report = week_report + "   No classes\n"
    if count >= 1:
        week_report = week_report + make_line(code1, start1, end1, conflict12 or conflict13 or conflict14)
    if count >= 2:
        week_report = week_report + make_line(code2, start2, end2, conflict12 or conflict23 or conflict24)
    if count >= 3:
        week_report = week_report + make_line(code3, start3, end3, conflict13 or conflict23 or conflict34)
    if count >= 4:
        week_report = week_report + make_line(code4, start4, end4, conflict14 or conflict24 or conflict34)

print("\n\n WEEKLY TIMETABLE ")
print(week_report)

print("CONFLICT REPORT ")
if conflict_count == 0:
    print("No conflicts found")
else:
    print(conflict_report)
    print("Total conflicts :", conflict_count)
