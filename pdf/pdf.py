import PyPDF2

file=open('twopage.pdf','rb')
reader=PyPDF2.PdfFileReader(file)
print(reader)

print(reader.getNumPages())

number_pages=reader.getPage(1)
print(number_pages)

print(reader.getDocumentInfo())
