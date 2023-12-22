OUTPUT_FILE_PATH = "artifacts/generated_table.tex"


def command(name, arg=None):
    command = f"\\{name}"
    if arg is not None:
        command += f"{{{arg}}}"
    return command


def generate_latex_table(input_list):
    if not all(len(row) == len(input_list[0]) for row in input_list):
        print("Table contains rows of different length")
        exit(1)

    def stringify_list(table):
        return [[str(value) for value in row] for row in table]

    stringified_list = stringify_list(input_list)

    table = command("begin", "tabular") + "{" + " c " * len(stringified_list[0]) + "}"
    for row in stringified_list[0:]:
        table += " & ".join(row) + " \\\\"
    table += command("end", "tabular")
    return table


def write_latex_table(input_list):
    table = generate_latex_table(input_list)
    with open(OUTPUT_FILE_PATH, "w") as f:
        f.write(table)


if __name__ == "__main__":
    test_list = [
        ["1", "2", "3"],
        [1, "Vasya", 3],
        ["Petya", 69.69, "Larisa"],
        [42, 42, "Roma"]
    ]
    write_latex_table(test_list)
