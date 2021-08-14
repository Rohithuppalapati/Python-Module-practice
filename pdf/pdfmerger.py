import PyPDF2

pdfs=['dummy.pdf','twopage.pdf','wtr.pdf']

def merger_of_pdfs(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('clubbed_pdf.pdf')

merger_of_pdfs(pdfs)
