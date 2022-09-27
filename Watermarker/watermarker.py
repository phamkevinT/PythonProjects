import PyPDF2

# PDF that needs watermark added
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# Watermark
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# Newly watermarked PDF
output = PyPDF2.PdfFileWriter

for i in range(template.getNumPages()):
    # Get each page in the original PDF
    page = template.getPage(i)
    # Merge page with the watermark
    page.mergePage(watermark.getPage(0))
    # Add newly watermarked page to final PDF
    output.addPage(page)

    # Write the watermarked PDF to file
    with open('watermarked_output.py', 'wb') as file:
        output.write(file)
