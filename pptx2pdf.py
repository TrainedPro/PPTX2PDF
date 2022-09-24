import glob, os
from PyPDF2 import PdfFileMerger

# Folder To All The PDFs
inputfldr = 'C:/Users/Naveed/Downloads/PF Lectures'

os.chdir(inputfldr)

print('Directory Changed To:', inputfldr)

print(f'ppt2pdf dir .')
os.system(f'ppt2pdf dir .')

dellst = []

merger = PdfFileMerger()
for pptx in glob.iglob(inputfldr + '/*.pdf'):
    merger.append(pptx)
    dellst.append(pptx)

# Will Merge All The PDFs
merger.write(f"{inputfldr}/merged_all_pages.pdf")
merger.close()

# Will Delete The Individual PDFs
for file in dellst:
    os.remove(file)
