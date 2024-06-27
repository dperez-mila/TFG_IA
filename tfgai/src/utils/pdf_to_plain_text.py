import io, requests
import fitz

def pdf_content_from_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status() 
    pdf_stream = io.BytesIO(response.content)
    doc = fitz.open(stream=pdf_stream, filetype="pdf")
    return _extract_pdf_content(doc)

def pdf_content_from_file_path(file_path: str) -> str:
    doc = fitz.open(file_path)
    return _extract_pdf_content(doc)

def _extract_pdf_content(doc: fitz.Document):
    content = ''
    for page in doc:
        content += page.get_text()
    return content

