from fastapi import FastAPI, UploadFile, File
import pdfplumber

app = FastAPI()

@app.post("/extract.pdf/")
async def extract_pdf(file: UploadFile = File(...)):
    content = []

    with pdfplumber.open(file.file) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            content.append({"page number": i + 1, "text": text})

    return {"pages": content}

