import fitz  # PyMuPDF

def extract_pdf_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file: '{pdf_path}'")

    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
