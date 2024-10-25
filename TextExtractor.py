import pdfplumber  # Ensure pdfplumber is installed

def extract_text_from_pdf(pdf_path):
    text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through each page
        for page in pdf.pages:
            # Extract text from the page
            text += page.extract_text() + "\n"  # Add a newline for separation
            
    return text

# Usage
if __name__ == "__main__":
    pdf_path = r"C:\\Users\\ANISH GARG\\Downloads\\py-vscode.pdf"  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
