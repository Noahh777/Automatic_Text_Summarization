import PyPDF2

def pdf_to_text(file):

    pdffile = open(file,'rb')

    pdfReader = PyPDF2.PdfReader(pdffile)

    num = len(pdfReader.pages)

    for i in range(0,num):
        pageobj = pdfReader.pages[i]
        resulttext = pageobj.extract_text()
        newfile = open(r"content.txt", "w")
        newfile.writelines(resulttext)
    
    demo=open("content.txt","r")
    str1=demo.read()
    return str1
