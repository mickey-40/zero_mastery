import PyPDF2
import sys

inputs = sys.argv
# print(inputs[1])
# print(inputs[2])

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs[1:])