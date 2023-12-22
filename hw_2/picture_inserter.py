from hw_2 import generate_latex_table, command

OUTPUT_FILE_PATH = "artifacts/generated_table_and_image.tex"
IMAGE_PATH = "Chilintano.jpg"


def write_latex_table_and_image(input_list):
    doc = command("documentclass", "article")
    doc += command("usepackage", "graphicx")
    doc += command("begin", "document")
    doc += generate_latex_table(input_list)
    doc += command("includegraphics") + "[width=0.4\\textwidth]" + f"{{{IMAGE_PATH}}}"
    doc += command("end", "document")
    with open(OUTPUT_FILE_PATH, "w") as f:
        f.write(doc)


if __name__ == "__main__":
    test_list = [
        [69, 42, 69],
        [69, 42, 69],
        [69, 42, 69],
    ]
    write_latex_table_and_image(test_list)
