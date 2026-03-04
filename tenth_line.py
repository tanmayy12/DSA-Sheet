def print_tenth_line(filename):
    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):
            if i == 10:
                print(line.strip())
                return