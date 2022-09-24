import glob, os
from PyPDF2 import PdfFileMerger

# Folder To All The PDFs
inputfldr = 'C:/Users/Naveed/Downloads/PF Lectures'

os.chdir(inputfldr)

print('Directory Changed To:', inputfldr)

os.system(f'ppt2pdf dir .')

# List To Delete All The Individual ".pdf" Files
dellst = []

merger = PdfFileMerger()

# Loop To Gather All ".pdf" Files In The inputflder
for pptx in glob.iglob(inputfldr + '/*.pdf'):
    merger.append(pptx)
    dellst.append(pptx)

# Will Merge All The PDFs
merger.write(f"{inputfldr}/MergedDocument.pdf")
merger.close()

# Will Delete The Individual PDFs
for file in dellst:
    os.remove(file)
