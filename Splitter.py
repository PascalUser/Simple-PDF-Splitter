import sys
import os

def get_pdf_paths(input_path):
    """Returns a list of PDF file paths from the given input path."""
    if not os.path.exists(input_path):
        print(f"Path does not exist: {input_path}")
        sys.exit(1)
    if os.path.isfile(input_path) and input_path.lower().endswith('.pdf'):
        return [input_path]
    elif os.path.isdir(input_path):
        pdf_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.lower().endswith('.pdf')]
        if not pdf_files:
            print("No PDF files found in the folder.")
            sys.exit(1)
        return pdf_files
    else:
        print("Input must be a PDF file or a folder containing PDF files.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Splitter.py <PDF file or folder>")
        sys.exit(1)
    input_path = sys.argv[1]
    pdf_paths = get_pdf_paths(input_path)
    print("PDF files to process:")
    for pdf in pdf_paths:
        print(pdf)
        
        