import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_compiner(pdf_list,file_name):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(f'{file_name}.pdf')
        
        
file_name = str(input('Enter Your new file name : '))
pdf_compiner(inputs,file_name)