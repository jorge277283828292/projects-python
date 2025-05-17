#Crea un word deacuerdo a un plantilla y con la informacion que se le sea brindada.
import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

nombre = "Jorge Villarreal"
telefono = "(123) 456-789"
correo = "jls@gmail.com"
fecha = datetime.today().strftime("%d/%m/%Y")

print(fecha)

constantes = {'nombre': nombre, 'telefono': telefono, 'correo': correo, 'fecha': fecha}

documento = DocxTemplate("plantilla.docx")
documento.render(constantes)
documento.save("prueba.docx")

df = pd.read_excel('Alumnos.xlsx')

for indice, fila in df.iterrows():
    contenido = {
        'nombre_alumno': fila["Nombre del Alumno"],
        'nota_mat': fila['Mat'],
        'nota_fis': fila['Fis'],
        'nota_qui': fila['Qui']
    }
    contenido.update(constantes)
    doc_alumno = DocxTemplate("plantilla.docx")
    doc_alumno.render(contenido)
    doc_alumno.save(f"notas_de_{fila['Nombre del Alumno']}.docx")
    print(contenido)