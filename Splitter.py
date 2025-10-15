import sys
import os
from PyPDF2 import PdfReader, PdfWriter

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

def split_pdf_files(pdf_paths, pages_per_split, use_folders=False):
    """Splits each PDF in pdf_paths into parts with pages_per_split pages."""
    for pdf_path in pdf_paths:
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        base_dir = os.path.dirname(pdf_path)

        # Create a folder for splits if the flag is enabled
        if use_folders:
            output_dir = os.path.join(base_dir, f"{base_name} - Splitted")
            os.makedirs(output_dir, exist_ok=True)
        else:
            output_dir = base_dir

        part = 1
        for start in range(0, total_pages, pages_per_split):
            writer = PdfWriter()
            end = min(start + pages_per_split, total_pages)
            for i in range(start, end):
                writer.add_page(reader.pages[i])
            output_path = os.path.join(output_dir, f"{base_name} - Part {part}.pdf")
            with open(output_path, "wb") as out_file:
                writer.write(out_file)
            part += 1

        print(f"{base_name} split into {part - 1} parts. Saved in: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python Splitter.py <PDF file or folder> <pages per split> [--use-folders]")
        sys.exit(1)
        
    # Get input path and pages per split
    input_path = sys.argv[1]
    pages_per_split = int(sys.argv[2])
    use_folders = len(sys.argv) == 4 and sys.argv[3] == "--use-folders"

    # Get PDF paths
    pdf_paths = get_pdf_paths(input_path)
    
    # Split PDF files
    split_pdf_files(pdf_paths, pages_per_split, use_folders)
    
    print("PDF splitting completed.")
