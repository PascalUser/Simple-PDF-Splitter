# Simple PDF Splitter
Simple Python script that splits PDF files into smaller parts.
It takes two arguments:
- Path — either a single PDF file or a folder containing multiple PDFs.
- Maximum number of pages per output file.

The script will automatically split each PDF in the given path into multiple files named like:

``` example.pdf → example - Part 1.pdf, example - Part 2.pdf, ...```
## Usage
```python Splitter.py <PDF file or folder> <pages per split>```

Example:
```python Splitter.py ./Documents 10```

## Features
Works with both single PDFs and entire folders
Keeps original filenames with numbered parts
Simple, dependency-light (only requires PyPDF2)
