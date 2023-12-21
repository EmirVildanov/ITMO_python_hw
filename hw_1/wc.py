import sys


def count_lines(lines):
    newlines_counter = 0
    words_counter = 0
    bytes_counter = 0
    for line in lines:
        if line.endswith("\n"):
            newlines_counter += 1
        words_counter += len(line.split())
        bytes_counter += len(line)
    return newlines_counter, words_counter, bytes_counter


def count_file(file_name):
    try:
        with open(file_name) as f:
            return count_lines(f.readlines())
    except FileNotFoundError:
        print(f"File {file_name} doesn't exist")
        exit(1)


def print_formatted(newlines, words, bytes, name=None):
    if name is None:
        print(f"\t{newlines}\t{words}\t{bytes}")
    else:
        print(f"{newlines} {words} {bytes} {name}")


if __name__ == "__main__":
    # Print  newline,  word,  and  byte  counts for each FILE, and a total line if more than one FILE is specified.
    # A word is a non-zero-length sequence of characters delimited by white space.
    args_number = len(sys.argv)
    if args_number == 1:
        # Reading from std.
        # Note: use Ctrl + D to send EOF to stdin.
        std_input_lines = []
        for line in sys.stdin:
            std_input_lines.append(line)
        newlines, words, bytes = count_lines(std_input_lines)
        print_formatted(newlines, words, bytes)
    elif args_number == 2:
        # One file passed. No total stats needed.
        file_name = sys.argv[1]
        newlines, words, bytes = count_file(file_name)
        print_formatted(newlines, words, bytes, file_name)
    else:
        # Several files passed. Total stats needed.
        total_lines = 0
        total_words = 0
        total_bytes = 0
        for file_index in range(1, args_number):
            file_name = sys.argv[file_index]
            newlines, words, bytes = count_file(sys.argv[file_index])
            print_formatted(newlines, words, bytes, file_name)
            total_lines += newlines
            total_words += words
            total_bytes += bytes
        print_formatted(total_lines, total_words, total_bytes, "total")
