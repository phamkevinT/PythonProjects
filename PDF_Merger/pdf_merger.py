import PyPDF2
import sys

# Take the first to last PDF in terminal input
inputs = sys.argv[1:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    # Get each PDF and merge
    for pdf in pdf_list:
        merger.append(pdf)
    # Write the merged PDF into new PDF
    merger.write('merged_pdf.pdf')


pdf_merger(inputs)
