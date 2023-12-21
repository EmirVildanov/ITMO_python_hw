import sys

if __name__ == "__main__":
    args_number = len(sys.argv)
    input_lines = []
    if args_number == 1:
        # Reading from stdin.
        # Note: use Ctrl + D to send EOF to stdin.
        for line in sys.stdin:
            input_lines.append(line)
    elif args_number == 2:
        # Reading from file.
        file_name = sys.argv[1]
        try:
            with open(file_name) as f:
                for line in f.readlines():
                    input_lines.append(line)
        except FileNotFoundError:
            print(f"File {file_name} not found")
            exit(1)
    else:
        print(f"Usage: custom_nl [file_name]")
        exit(1)

    for i, line in enumerate(input_lines):
        print(f"\t{i + 1} {line.rstrip()}")