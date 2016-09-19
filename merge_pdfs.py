#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
from pyPdf import PdfFileReader, PdfFileWriter
import os


def merge(path, output_filename, merge_whole_directory=False):
	if merge_whole_directory:
	    pdfs = []
	    for pdf_file in glob(path + os.sep + '*.pdf'):
	        pdfs.append(pdf_file)
	else:
	    pdfs = path.split(',') 		
	output = PdfFileWriter()
	if len(pdfs) == 0:
	    print("No files to merge")
	    return
	for pdf in pdfs:
	    if pdf == output_filename:
	        continue
            print("Parse '%s'" % pdf)
            document = PdfFileReader(open(pdf, 'rb'))
            for i in range(document.getNumPages()):
                output.addPage(document.getPage(i))
        print("Start writing '%s'" % output_filename)
        with open(output_filename, "wb") as f:
            output.write(f)

if __name__ == "__main__":
    parser = ArgumentParser()

    # Add more options if you like
    parser.add_argument("-o", "--output",
                        dest="output_filename",
                        default="merged.pdf",
                        help="file to write merged PDF's",
                        metavar="FILE")
    parser.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files separeted by comas")
    parser.add_argument("-a", "--all",
                        dest="all",
                        action='store_true',
                        help="if to merge all files from path")
                        
    args = parser.parse_args()
    merge(args.path, args.output_filename, args.all)
