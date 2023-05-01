import multiprocessing
from PyPDF4 import PdfFileReader
import subprocess
import time





def do_job(page_number):
    subprocess.call(['mutool', 'draw', '-G1.1', '-c', 'g',
                    '-i', '-P', '-r120', '-o', 'extracted/' + str(page_number) + '.png', 
                    "pdf/Edgar_Allan_Poe.pdf", str(page_number)])


def main():
    
    #get number of pages:
    pdf = PdfFileReader(open("pdf/Edgar_Allan_Poe.pdf",'rb'))
    number_of_pages = int(pdf.getNumPages())
    print(number_of_pages)

    start_time = time.time()

    processes = []
    for i in range(1, number_of_pages):
        p = multiprocessing.Process(target=do_job, args=( i,))
        processes.append(p)
        p.start()
        #all the job is done between these lines
    for process in processes:
        process.join()
    
    #calculate the execution time:
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_rounded = round(elapsed_time, 2)

    print("Elapsed time: ", elapsed_time_rounded, "seconds")


if __name__ == '__main__':
    main()
