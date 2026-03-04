def print_tenth_line(filename):
    with open(filename) as f:
        lines = f.readlines()
        if len(lines) >= 10:
            print(lines[9].strip())