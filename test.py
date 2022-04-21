import os
from PyPDF2 import PdfFileMerger
target_path=input('input_path=')
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]
file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)
out_path=input('out_path=')
out_name=input('out_name=')
out_file=out_path+out_name
file_merger.write(out_file)
