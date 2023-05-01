import subprocess
from PyPDF4 import PdfFileReader
import time

def extract(number_of_pages):
    for page_number in range(1, number_of_pages):
        subprocess.call(['mutool', 'draw', '-G1.1', '-c', 'g',
                    '-i', '-P', '-r120', '-o', 'extracted/' + str(page_number) + '.png', 
                    "pdf/Edgar_Allan_Poe.pdf", str(page_number)])


#get number of pages:
pdf = PdfFileReader(open("pdf/Edgar_Allan_Poe.pdf",'rb'))
number_of_pages = int(pdf.getNumPages())
#print(number_of_pages)


start_time = time.time()
extract(number_of_pages)


#calculate the execution time:
end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_rounded = round(elapsed_time, 2)

print("Elapsed time: ", elapsed_time_rounded, "seconds")


