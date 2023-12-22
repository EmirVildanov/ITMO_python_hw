In order to generate .pdf file from previously generate .tex, run the following commands:

1. `bash`
2. `docker build -t pdfbuilder .`
3. `docker run --rm --volume "`pwd`:/data" pdfbuilder artifacts/generated_table_and_image.tex`
`