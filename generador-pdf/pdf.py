#Genera un PDF con la informacion indicada.
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if hasattr(self, 'document_title'):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, self.document_title, 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font(family='Arial', style='I', size=8)
        self.cell(w=0, h=10, txt=f'Página {self.page_no()}', border=0, ln=0, align='C')
        
    def chapter_title(self, title, font='Arial', size=12):
        self.set_font(font, style='B', size=size)
        self.cell(w=0, h=10, txt=title, border=0, ln=1, align='L')
        self.ln(10)

    def chapter_body(self, body, font='Arial', size=12):
        self.set_font(font, style='', size=size)
        self.multi_cell(w=0, h=10, txt=body)
        self.ln()

def create_pdf(filename, document_title, author, chapters, image_path=None):
    pdf = PDF()
    pdf.document_title = document_title
    pdf.add_page()
    if author:
        pdf.set_author(author)

    if image_path:
        pdf.image(image_path, x=10, y=25, w=pdf.w - 20)
        pdf.ln(120)

    for chapter in chapters:
        pdf.chapter_title(chapter['title'])
        pdf.chapter_body(chapter['body'])

    pdf.output(filename, 'F')

def main():
    chapters = [
        {"title": "Introducción", "body": "Este es el primer capítulo del PDF generado con Python."},
        {"title": "Contenido", "body": "Aquí puedes agregar el contenido que desees en tu PDF."}
    ]
    create_pdf(
        filename="ejemplo.pdf",
        document_title="Mi Documento PDF",
        author="Tu Nombre",
        chapters=chapters
    )
    print("PDF generado exitosamente.")

if __name__ == "__main__":
    main()