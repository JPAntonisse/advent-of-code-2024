import os


def read_input(day):
    """
    Reads the input file for a given day.
    :param day: int, the day number.
    :return: List of lines from the input file.
    """
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))  # Ensure __file__ is valid.
    except NameError:
        base_path = os.getcwd()

    inputs_dir = os.path.join(base_path, "../inputs")

    file_name = f"day{day:02}.txt"
    file_path = os.path.normpath(os.path.join(inputs_dir, file_name))

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found for Day {day}: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except Exception as e:
        raise IOError(f"Error reading file {file_path}: {e}")
