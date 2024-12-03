import numpy as np

from utils.file_reader import read_input

reports = np.array(read_input(day=2))


# a report only counts as safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# How many reports are save?

def is_report_save(report):
    # Get the differential
    differential = np.diff(report)

    # All increasing?
    # Either only increasing (true) or decreasing (false)
    is_increasing = np.all(differential > 0)
    is_decreasing = np.all(differential < 0)
    is_moving = is_decreasing or is_increasing

    # Differ min 1, max 3
    is_adjacent = np.all((abs(differential) >= 1) & (abs(differential) <= 3))

    return is_moving and is_adjacent


save = []
for report in reports:
    # Convert to array integers
    report = np.array(report.split(' ')).astype(int)
    # Check if report is save
    save.append(is_report_save(report=report))

# Count good reports
save_reports = np.count_nonzero(save)
print(f"Save reports: {save_reports}")


# Part two
# Problem dampener, single bad level
# If a single level can be removed to make it safe, it is safe

# So it is acceptable to have:
# 1 Level that is not increasing / decreasing
# 1 level that differs the min 1, max 3

def is_report_dampening(report):
    """
    Checks if the report can pass by dampening
    :param report:
    """
    print()
    print(report)
    # Get the differential
    for index, level in enumerate(report):
        # Exclude the current element using np.delete
        temp_report = np.delete(report, index)
        print(temp_report)

        # Check if valid
        if is_report_save(report=temp_report):
            return True

    return False

not_save_index = np.array([i for i, val in enumerate(save) if not val])

can_dampening = []
for not_save in not_save_index:
    report = reports[not_save]
    # Convert to array integers
    report = np.array(report.split(' ')).astype(int)
    # Check if report can be dampened
    can_dampening.append(is_report_dampening(report=report))

dampening_count = np.count_nonzero(can_dampening)

save_reports_dampening = save_reports + dampening_count
print(save_reports_dampening)