from PyPDF4 import PdfFileReader


#get number of pages:
pdf = PdfFileReader(open("pdf/Edgar_Allan_Poe.pdf",'rb'))
number_of_pages = int(pdf.getNumPages())
print(number_of_pages)
