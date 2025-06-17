from pathlib import Path
from PyPDF2 import PdfReader
import markdownify
pdf_path = Path("haroon_resume.pdf")  
reader = PdfReader(pdf_path)
for page in reader.pages:
    text = page.extract_text()
print(markdownify.markdownify(text))