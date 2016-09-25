#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def split(path):
	if len(path) > 1:
		split_whole_directory = False
	else:
		split_whole_directory = True
	if split_whole_directory:
	    pdfs = []
	    for pdf_file in glob(path + os.sep + '*.pdf'):
	        pdfs.append(pdf_file)
	else:
	    pdfs = path.split(',') 		
	if len(pdfs) == 0:
	    print("No files to merge")
	    return
	for pdf in pdfs:
		inputpdf = PdfFileReader(file(pdf, "rb"))    
        for i in range(inputpdf.numPages): 
			output = PdfFileWriter()
			output.addPage(inputpdf.getPage(i))
			if i + 1 <  inputpdf.numPages:
				output.addPage(inputpdf.getPage(i + 1))
			newname = pdf[:7] + "-" + str(i) + ".pdf"
			outputStream = file(newname, "wb")
			output.write(outputStream)
			outputStream.close()

if __name__ == "__main__":
    parser = ArgumentParser()

    # Add more options if you like
    parser.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files separeted by comas")
                        
    args = parser.parse_args()
    split(args.path)
