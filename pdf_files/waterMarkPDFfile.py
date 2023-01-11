import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf','rb'))
waterMark = PyPDF2.PdfReader(open('water-mark.pdf','rb'))
output =PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(waterMark.pages[0])
    output.add_page(page)
    
with open('waterMarked-output.pdf','wb') as new_file:
    output.write(new_file)