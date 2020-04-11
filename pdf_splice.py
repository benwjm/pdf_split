from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import *
from tkinter import filedialog

def browse():
    filename = filedialog.askopenfilename()
    filename_entry.insert(0,filename)
    
def submit():
    filename = filename_entry.get()
    pagenums = pagenums_entry.get()
    pagenums = pagenums.split('-')
    start = int(pagenums[0])
    end = int(pagenums[1])
    output_name = output_entry.get()
    pdf = PdfFileReader(filename)
    pdf_writer = PdfFileWriter()

    for i in range(start, end+1):
        pdf_writer.addPage(pdf.getPage(i))

    output = f'{output_name}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

root = tk.Tk()
root.title('Split PDF File into Pages')
root.attributes("-topmost", "true")

window = tk.Canvas(root, width=300, height=260)
window.pack()

filename_label = tk.Label(root, text="Select file (pdf)")
window.create_window(150, 40, window=filename_label)
filename_entry = tk.Entry(root)
window.create_window(150, 60, window=filename_entry)

browse_button = tk.Button(text='Browse', command=browse)
window.create_window(240, 60, window=browse_button)

pagenums_label = tk.Label(root, text="Enter page numbers i.e., 5-7")
window.create_window(150, 100, window=pagenums_label)
pagenums_entry = tk.Entry(root)
window.create_window(150, 120, window=pagenums_entry)

output_label = tk.Label(root, text="Enter name of output file")
window.create_window(150, 160, window=output_label)
output_entry = tk.Entry(root)
window.create_window(150, 180, window=output_entry)

submit_pagenums = tk.Button(text='Submit', command=submit)
window.create_window(150, 220, window=submit_pagenums)

root.mainloop()
