import io, requests, fitz

def extract_text_from_pdf_url(url) -> str:
    response = requests.get(url)
    response.raise_for_status() 
    pdf_stream = io.BytesIO(response.content)
    doc = fitz.open(stream=pdf_stream, filetype="pdf")
    text = ''
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

