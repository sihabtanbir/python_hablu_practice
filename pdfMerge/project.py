from PyPDF2 import PdfMerger

AllPdf = ['1st.pdf', '2nd.pdf']

ourMerger = PdfMerger()

for newPdf in AllPdf:
    ourMerger.append(newPdf)

ourMerger.write('merge.pdf')
ourMerger.close()