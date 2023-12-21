import sys


def print_last_n_stripped(lines, n):
    for last_line in lines[-n:]:
        print(last_line.rstrip())


def write_file(file_name, write_name=False, add_newline=False):
    try:
        with open(file_name) as f:
            if add_newline:
                print()
            if write_name:
                print(f"==> {file_name} <==")
            print_last_n_stripped(f.readlines(), 10)
    except FileNotFoundError:
        print(f"File {file_name} not found")
        exit(1)


if __name__ == "__main__":
    args_number = len(sys.argv)
    if args_number == 1:
        # Reading from std.
        # Note: use Ctrl + D to send EOF to stdin.
        std_input_lines = []
        for line in sys.stdin:
            std_input_lines.append(line)
        print_last_n_stripped(std_input_lines, 17)
    elif args_number == 2:
        # Reading from file. No formatting needed.
        file_name = sys.argv[1]
        write_file(file_name)
    else:
        # Reading from several files. Formatting needed.
        for file_index in range(1, args_number):
            file_name = sys.argv[file_index]
            write_file(file_name, True, file_index != 1)