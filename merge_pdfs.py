#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger, PdfFileReader
import os


def merge(path, output_filename):
        if len(path) > 1:
                merge_whole_directory = False
        else:
                merge_whole_directory = True
	if merge_whole_directory:
	    pdfs = []
	    for pdf_file in glob(path + os.sep + '*.pdf'):
	        pdfs.append(pdf_file)
	else:
	    pdfs = path.split(',') 		
	if len(pdfs) == 0:
	    print("No files to merge")
	    return
	merger = PdfFileMerger(strict=False)
	for pdf in pdfs:
	    if pdf == output_filename:
	        continue
            print("Parse '%s'" % pdf)
            merger.append(PdfFileReader(file(pdf, 'rb')))
        print("Start writing '%s'" % output_filename)
        merger.write(output_filename)

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
                        
    args = parser.parse_args()
    merge(args.path, args.output_filename)
