import fitz  # PyMuPDF

def load_pdf(file_path: str) -> str:
    """
    Extract raw text from a PDF file.
    """
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text