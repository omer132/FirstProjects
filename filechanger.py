from pdf2docx import Converter

pdf_file = "CU18M - CU18W 1.tur.pdf"
docx_file = "CU18M - CU18W 1.tur.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()