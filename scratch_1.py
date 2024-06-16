import fitz  # PyMuPDF
import os
def merge_pdfs(output_path, input_paths):
    # Create a Document object to hold the merged PDF
    merged_document = fitz.open()

    for path in input_paths:
        # Open each PDF file
        pdf_document = fitz.open(path)
        # Add all pages from the current PDF to the merged document
        merged_document.insert_pdf(pdf_document)

    # Save the merged document to the specified output path
    merged_document.save(output_path)
    # Close the merged document
    merged_document.close()

if __name__ == "__main__":
    input_directory = r"C:\Users\gilim\Downloads\לומדות\תרגולים"  # Change this to the directory containing your PDF files
    output_path = os.path.join(input_directory,"output_merged_file.pdf")     # Change this to the desired output file path

    # Get paths of all PDF files in the input directory
    input_paths = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.pdf')]

    # Merge PDFs
    merge_pdfs(output_path, input_paths)

    print("PDF files merged successfully!")