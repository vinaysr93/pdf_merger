import PyPDF2
import os
import sys


class Pdf_Merge():

    '''Class that is used to merge two PDF's'''
    def __init__(self,file1,page_1,file2,page_2):

        self.file1=file1
        self.file2=file2
        self.page_1=page_1
        self.page_2=page_2

    def get_info(self):

       with open(self.file1,'rb') as file1 :
            reader1=PyPDF2.PdfFileReader(file1)
            print(reader1.numPages)

       with open(self.file2,'rb') as file2:
           reader2=PyPDF2.PdfFileReader(file2)
           print(reader2.numPages)


    def merge_files(self):


        new_pdf=input("Please input the new file name")

        output=PyPDF2.PdfFileWriter()


        for page_in_file1 in range(self.page_1[0],self.page_1[1]+1):
            output.addPage(PyPDF2.PdfFileReader(self.file1,"rb").getPage(page_in_file1))

        for page_in_file2 in range(self.page_2[0],self.page_2[1]+1):
            output.addPage(PyPDF2.PdfFileReader(self.file2,"rb").getPage(page_in_file2))


        with open(f"{new_pdf}.pdf","wb") as f:
            output.write(f)

q=Pdf_Merge("Network Setting Procedure ver 5.pdf",[0,0],"win XP Embedded.pdf",[0,0])
q.get_info()
q.merge_files()