import PyPDF2

input=open('clubbed_pdf.pdf','rb')
input_file=PyPDF2.PdfFileReader(input)
watermrk=PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(input_file.getNumPages()):
    page=input_file.getPage(i)
    page.mergePage(watermrk.getPage(0))
    output.addPage(page)

    wtrmrked=open('wtrmrked.pdf','wb')
    output.write(wtrmrked)
    print('run successful watermarked the file')

