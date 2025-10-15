# Simple PDF Splitter

Simple Python script that splits PDF files into smaller parts.
It takes two arguments:

* Path — either a single PDF file or a folder containing multiple PDFs.
* Maximum number of pages per output file.

The script will automatically split each PDF in the given path into multiple files named like:

```
example.pdf → example - Part 1.pdf, example - Part 2.pdf, ...
```

---

## Installation

Clone the repository and install the required dependency:

```bash
git clone https://github.com/PascalUser/Simple-PDF-Splitter.git
cd Simple-PDF-Splitter
pip install -r requirements.txt
```

---

## Usage

```bash
python Splitter.py <PDF file or folder> <pages per split> [--use-folders]
```

Examples:

```bash
python Splitter.py ./Example_folder 10
python Splitter.py ./Example_file.pdf 5 --use-folders
```

---

## Features

* Works with both single PDFs and entire folders
* Keeps original filenames with numbered parts
* Optional `--use-folders` flag to save parts into automatically created subfolders

  * Example:
      ```
    Chapter1 - Splitted/
      ├── Chapter1 - Part 1.pdf
      ├── Chapter1 - Part 2.pdf
      └── Chapter1 - Part 3.pdf
      ```



* Simple, dependency-light (only requires PyPDF2)
