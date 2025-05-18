import fitz  # PyMuPDF

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts and concatenates text from all pages of a PDF.

    Args:
        file_bytes (bytes): Raw bytes of the uploaded PDF.

    Returns:
        str: Full concatenated text content from the PDF.
    """
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        all_text = []
        for page in doc:
            text = page.get_text()
            if text:
                all_text.append(text.strip())
        return "\n\n".join(all_text)
    except Exception as e:
        return f"❌ Failed to extract text: {str(e)}"

def extract_metadata(file_bytes: bytes) -> dict:
    """
    Extracts metadata (title, author, etc.) from a PDF.

    Args:
        file_bytes (bytes): Raw bytes of the PDF.

    Returns:
        dict: Dictionary of metadata fields.
    """
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        return doc.metadata
    except Exception as e:
        return {"error": str(e)}
