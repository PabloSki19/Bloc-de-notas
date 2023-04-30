import glob
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as f
from tkinter import font
from tkinter import Menu
from tkinter import messagebox, filedialog, Toplevel, colorchooser
from tkinter.ttk import Combobox, Entry
from io import open

#Ventana
root = tk.Tk()
url_archivo = ""
title = "Bloc de notas"
root.title("Sin título.txt | " + title)
root.geometry("700x500")
icono = tk.PhotoImage(file="icons/icon-32.png")
root.iconphoto(False, icono)
info_estado = BooleanVar()
info_estado.set(False)

fuente_tipo = 'Arial'
fuente_tamaño = 12

#Funciones específicas
def nuevo_archivo(event=None):
    global url_archivo
    area_texto.delete(1.0, "end")
    url_archivo = ""
    root.title("Sin título.txt | " + title)

def abrir_archivo(event=None):
    global url_archivo
    url_archivo = f.askopenfilename(initialdir='.', title='Abrir', filetypes=(('Archivo de texto','txt'),('Todos los archivos','*.*')))
    if url_archivo != "":
        file = open(url_archivo, 'r')
        content = file.read()
        area_texto.delete(1.0, "end")
        area_texto.insert('insert', content)
        file.close()
        root.title(os.path.basename(url_archivo) + " | " + title)
    
    try:
        abierto = str(len(content))
        archivo_abrir_guardar = open("data/archivo.txt", "w")
        archivo_abrir_guardar.write(abierto)
        archivo_abrir_guardar.close()
    except:
        pass

def salir(event=None):
    try:
        contenido = str(len(area_texto.get(1.0,'end-1c')))
        archivo_abierto = open("data/archivo_abierto.txt", "w")
        archivo_abierto.write(contenido)
        archivo_abierto.close()
    except:
        pass

    archivo_abrir_guardar = open("data/archivo.txt", "r")
    contenido_inicial = archivo_abrir_guardar.read()
    archivo_abrir_guardar.close()

    archivo_abierto = open("data/archivo_abierto.txt", "r")
    contenido_final = archivo_abierto.read()
    archivo_abierto.close()

    if len(area_texto.get(1.0,'end-1c')) > 0:
        if contenido_inicial != contenido_final:
            valor = messagebox.askyesnocancel(message="¿Quieres guardar los cambios?", title="Bloc de notas")
            if valor == True:
                guardar()
            elif valor == False:
                pass
            else:
                return
        root.destroy()
    else:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", salir)

#Funciones generales
def nuevo(event=None):
    try:
        contenido = str(len(area_texto.get(1.0,'end-1c')))
        archivo_abierto = open("data/archivo_abierto.txt", "w")
        archivo_abierto.write(contenido)
        archivo_abierto.close()
    except:
        pass

    archivo_abrir_guardar = open("data/archivo.txt", "r")
    contenido_inicial = archivo_abrir_guardar.read()
    archivo_abrir_guardar.close()

    archivo_abierto = open("data/archivo_abierto.txt", "r")
    contenido_final = archivo_abierto.read()
    archivo_abierto.close()
    
    if len(area_texto.get(1.0,'end-1c')) > 0:
        if contenido_inicial != contenido_final:
            valor = messagebox.askyesnocancel(message="¿Quieres guardar los cambios?", title="Bloc de notas")
            if valor == True:
                guardar()
            elif valor == False:
                pass
            else:
                return
        nuevo_archivo()
    else:
        nuevo_archivo

def abrir(event=None):
    try:
        contenido = str(len(area_texto.get(1.0,'end-1c')))
        archivo_abierto = open("data/archivo_abierto.txt", "w")
        archivo_abierto.write(contenido)
        archivo_abierto.close()
    except:
        pass

    archivo_abrir_guardar = open("data/archivo.txt", "r")
    contenido_inicial = archivo_abrir_guardar.read()
    archivo_abrir_guardar.close()

    archivo_abierto = open("data/archivo_abierto.txt", "r")
    contenido_final = archivo_abierto.read()
    archivo_abierto.close()
    
    if len(area_texto.get(1.0,'end-1c')) > 0:
        if contenido_inicial != contenido_final:
            valor = messagebox.askyesnocancel(message="¿Quieres guardar los cambios?", title="Bloc de notas")
            if valor == True:
                guardar()
            elif valor == False:
                pass
            else:
                return
        abrir_archivo()
    else:
        abrir_archivo()

def guardar(event=None):
    global url_archivo
    if url_archivo != "":
        content = area_texto.get(1.0, "end-1c")
        file = open(url_archivo, 'w+')
        file.write(content)
        root.title(os.path.basename(url_archivo) + " | " + title)
        file.close()
    else:
        file = f.asksaveasfile(title="Guardar como", mode="w", defaultextension='.txt', filetypes=(('Archivo de texto','txt'),('Todos los archivos','*.*')))
        if file is not None:
            url_archivo = file.name
            content = area_texto.get(1.0, "end-1c")
            file = open(url_archivo, 'w+')
            file.write(content)
            root.title(os.path.basename(url_archivo) + " | " + title)
            file.close()
    
    try:
        abierto = str(len(content))
        archivo_abrir_guardar = open("data/archivo.txt", "w")
        archivo_abrir_guardar.write(abierto)
        archivo_abrir_guardar.close()
    except:
        pass

def guardar_como(event=None):
    global url_archivo
    file = f.asksaveasfile(title="Guardar como", mode="w", defaultextension='.txt', filetypes=(('Archivo de texto','txt'),('Todos los archivos','*.*')))
    if file is not None:
        url_archivo = file.name
        content = area_texto.get(1.0, "end-1c")
        file = open(url_archivo, 'w+')
        file.write(content)
        root.title(os.path.basename(url_archivo) + " | " + title)
        file.close()
    
    try:
        abierto = str(len(content))
        archivo_abrir_guardar = open("data/archivo.txt", "w")
        archivo_abrir_guardar.write(abierto)
        archivo_abrir_guardar.close()
    except:
        pass

def deshacer(event=None):
    try:
        area_texto.edit_undo()
    except:
        pass

def rehacer(event=None):
    try:
        area_texto.edit_redo()
    except:
        pass

def cortar(event=None):
    root.focus_get().event_generate("<<Cut>>")

def copiar(event=None):
    root.focus_get().event_generate("<<Copy>>")

def pegar(event=None):
    root.focus_get().event_generate("<<Paste>>")

def eliminar(event=None):
    root.focus_get().event_generate("<<Clear>>")

def buscar_reemplazar(event=None):
    def encontrar_palabras():
        area_texto.tag_remove('match',1.0,END)
        iniciar_pos='1.0'
        palabra=entry_buscar.get()
        if palabra:
            while True:
                iniciar_pos = area_texto.search(palabra,iniciar_pos,stopindex=END)
                if not iniciar_pos:
                    break
                terminar_pos = f'{iniciar_pos}+{len(palabra)}c'
                area_texto.tag_add('match',iniciar_pos,terminar_pos)
                area_texto.tag_config('match',foreground='white',background='blue')
                iniciar_pos = terminar_pos

    def reemplazar_texto():
        palabra = entry_buscar.get()
        reemplazar_texto = entry_reemplazar.get()
        contenido = area_texto.get(1.0,END)
        nuevo_contenido = contenido.replace(palabra,reemplazar_texto)
        area_texto.delete(1.0,END)
        area_texto.insert(1.0,nuevo_contenido)
    
    ventana_buscar = Toplevel()
    ventana_buscar.resizable(0,0)
    ventana_buscar.geometry('350x250')
    ventana_buscar.title('Buscar / Reemplazar')

    label_frame = LabelFrame(ventana_buscar,text='Buscar / Reemplazar')
    label_frame.pack(pady=50)

    label_buscar = Label(label_frame,text='Buscar:')
    label_buscar.grid(row=0,column=0,padx=5,pady=5)
    entry_buscar = Entry(label_frame)
    entry_buscar.grid(row=0,column=1,padx=5,pady=5)

    label_reemplazar = Label(label_frame, text='Reemplazar:')
    label_reemplazar.grid(row=1, column=0, padx=5, pady=5)
    entry_reemplazar = Entry(label_frame)
    entry_reemplazar.grid(row=1,column=1,padx=5,pady=5)

    boton_buscar = Button(label_frame,text='Buscar',command=encontrar_palabras)
    boton_buscar.grid(row=2,column=0,padx=5,pady=5)

    boton_reemplazar = Button(label_frame,text='Reemplazar',command=reemplazar_texto)
    boton_reemplazar.grid(row=2,column=1,padx=5,pady=5)

    def do_something():
        area_texto.tag_remove('match',1.0,END)
        ventana_buscar.destroy()

    ventana_buscar.protocol('WM_DELETE_WINDOW',do_something)
    ventana_buscar.mainloop()

def seleccionar_todo(event=None):
    area_texto.tag_add('sel', '1.0', 'end')
    return "break"

def fondo_color():
    color = colorchooser.askcolor()[1]
    area_texto.config(bg= color)

def ayuda():
    ventana_ayuda = Toplevel()

    ventana_ayuda.resizable(0,0)
    ventana_ayuda.geometry("555x525")
    ventana_ayuda.title("Ayuda del Bloc de notas")

    texto_acerca = tk.Label(ventana_ayuda, text=("Ayuda del Bloc de notas"), font=('Arial',20,'bold','italic'))
    texto_acerca.place(x=50,y=10)

    imagen_ayuda = tk.PhotoImage(file="icons/ayuda-32.png")
    cargar_imagen = tk.Label(ventana_ayuda, image=imagen_ayuda).place(x=10,y=10)

    def pregunta_1():
        salida_texto.config(justify=tk.LEFT, text='El Bloc de notas es una aplicación que sirve para ver archivos de texto o realizar modificaciones en\nellos (por lo general, con una extensión .txt).')

    def pregunta_2():
        salida_texto.config(justify=tk.LEFT, text='Si se modifica el tamaño, tipo y estilo de la fuente, cambiará la apariencia de todo el texto del\narchivo, no solo de una parte.\n\n1. Abrir el Bloc de notas.\n2. Ir a la barra de herramientas.\n3. Seleccione un tipo de fuente, un estilo de fuente y un tamaño; y se cambiará automáticamente.\n\nIMPORTANTE: Cualquier modificación es sólo de muestra y va a ser mientras que corra el programa,\nno se van a grabar en el archivo txt.')

    def pregunta_3():
        salida_texto.config(justify=tk.LEFT, text='Para cambiar el color de fondo:\n1. Abrir el Bloc de notas.\n2. Haga clic en el menú Ver y, luego, en Color de fondo; o en el icono de la barra de herramientas\ncorrespondiente.\n3. Seleccione un color, y después haga clic en Aceptar.\n\nPara cambiar el color de texto:\n1. Abrir el Bloc de notas.\n2. Ir a la barra de herramientas, en el icono correspondiente.\n3. Seleccione un color, y después haga clic en Aceptar.\n\nIMPORTANTE: Cualquier modificación es sólo de muestra y va a ser mientras que corra el programa,\nno se van a grabar en el archivo txt.')

    def pregunta_4():
        salida_texto.config(justify=tk.LEFT, text='1. Abrir el Bloc de notas.\n2. Realice una de las acciones siguientes:\n\n• Para mover texto de un lugar a otro, selecciónelo, pulse o haga clic en el menú Editar y\ndespués pulse o haga clic en Cortar.\n• Para tener el mismo texto en dos lugares diferentes, selecciónelo, pulse o haga clic en el menú\nEditar y después pulse o haga clic en Copiar.\n• Para pegar texto que ha cortado o copiado, pulse o haga clic en el lugar del archivo donde desee\npegar el texto, pulse o haga clic en el menú Editar y después pulse o haga clic en Pegar.\n• Para eliminar texto, selecciónelo, pulse o haga clic en el menú Editar y después pulse o haga clic en\nEliminar.\n• Para deshacer la última acción, pulse o haga clic en el menú Editar y después pulse o haga clic en\nDeshacer.\n• Para rehacer la acción, pulse o haga clic en el menú Editar y después pulse o haga clic en Rehacer.\n\nTambién, se pueden realizar las acciones mencionadas anteriormente con los iconos de la barra de\nherramientas, según correspondan.')

    def pregunta_5():
        salida_texto.config(justify=tk.LEFT, text='Para buscar palabras o caracteres específicos:\n1. Abrir el Bloc de notas.\n2. Haga clic en el menú Editar y, luego, en Buscar / Reemplazar; o en el icono de la barra de\nherramientas correspondiente.\n3. En el cuadro Buscar, escriba los caracteres o las palabras que desee buscar.\n4. Haga clic en Buscar.\n\nPara reemplazar palabras o caracteres específicos:\n1. Abrir el Bloc de notas.\n2. Haga clic en el menú Editar y, luego, en Buscar / Reemplazar; o en el icono de la barra de\nherramientas correspondiente.\n3. En el cuadro Buscar, escriba los caracteres o las palabras que desee buscar.\n4. En el cuadro Reemplazar, escriba el texto de reemplazo.\n5. Haga clic en Buscar y, a continuación, en Reemplazar.')

    boton_pregunta_1 = Button(ventana_ayuda,text=("¿Qué consiste el Bloc de notas?"),command=pregunta_1,width=75).place(x=10,y=70)
    boton_pregunta_2 = Button(ventana_ayuda,text=("¿Cómo se cambia el tamaño, tipo y estilo de fuente?"),command=pregunta_2,width=75).place(x=10,y=100)
    boton_pregunta_3 = Button(ventana_ayuda,text=("¿Cómo se cambia el color de fondo o el color de texto?"),command=pregunta_3,width=75).place(x=10,y=130)
    boton_pregunta_4 = Button(ventana_ayuda,text=("¿Cómo se corta, copia, pega o elimina texto?"),command=pregunta_4,width=75).place(x=10,y=160)
    boton_pregunta_5 = Button(ventana_ayuda,text=("¿Cómo se buscan y reemplazan caracteres o palabras específicos?"),command=pregunta_5,width=75).place(x=10,y=190)

    salida_texto = tk.Label(ventana_ayuda)
    salida_texto.place(x=10, y=230)
    salida_texto.config(justify=tk.LEFT, text='¡Bienvenido a la Ayuda de Bloc de notas!\n\nHaz clic en uno de los botones para resolver su inquietud.')

    ventana_ayuda.mainloop()

def acerca_programa():
    ventana_acerca = Toplevel()
    ventana_acerca.resizable(0,0)
    ventana_acerca.geometry("325x275")
    ventana_acerca.title("Acerca del Bloc de notas")

    imagen_acerca = tk.PhotoImage(file="icons/logo.png")
    cargar_imagen = tk.Label(ventana_acerca, image=imagen_acerca)
    cargar_imagen.pack()
    texto_acerca = tk.Label(ventana_acerca, text=("Bloc de notas\nVersión 1.0\n2023\nPablo Aguilar")).place(x=125,y=100)
    boton_aceptar = tk.Button(ventana_acerca, text=("Aceptar"), width=10, command= lambda: ventana_acerca.destroy()).place(x=125,y=200)

    ventana_acerca.mainloop()

#Barra de estado
def barra_estado(event):
    palabras = len(area_texto.get(0.0,END).split())
    caracteres = len(area_texto.get(0.0,'end-1c').replace(' ',''))
    barra_de_estado.config(text=f'Caracteres: {caracteres}, Palabras: {palabras}')

    area_texto.edit_modified(False)

barra_de_estado = Label(root,text=' ')
barra_de_estado.pack(side=BOTTOM)

#Barra de menú
barra_menu = tk.Menu()

#Menú archivo
menu_archivo = tk.Menu(barra_menu, tearoff=False)
menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=nuevo)
menu_archivo.add_command(label="Abrir...", accelerator="Ctrl+O", command=abrir)
menu_archivo.add_command(label="Guardar", accelerator="Ctrl+S", command=guardar)
menu_archivo.add_command(label="Guardar como...", accelerator="Ctrl+Alt+S", command=guardar_como)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", accelerator="Ctrl+Q", command=salir)
barra_menu.add_cascade(menu=menu_archivo, label="Archivo")

#Menú edición
menu_edicion = tk.Menu(barra_menu, tearoff=False)
menu_edicion.add_command(label="Deshacer", accelerator="Ctrl+Z", command=deshacer)
menu_edicion.add_command(label="Rehacer", accelerator="Ctrl+Y", command=rehacer)
menu_edicion.add_separator()
menu_edicion.add_command(label="Cortar", accelerator="Ctrl+X", command=cortar)
menu_edicion.add_command(label="Copiar", accelerator="Ctrl+C", command=copiar)
menu_edicion.add_command(label="Pegar", accelerator="Ctrl+V", command=pegar)
menu_edicion.add_command(label="Eliminar", accelerator="Supr", command=eliminar)
menu_edicion.add_separator()
menu_edicion.add_command(label="Buscar / Reemplazar", accelerator="Ctrl+F", command=buscar_reemplazar)
menu_edicion.add_separator()
menu_edicion.add_command(label="Seleccionar todo", accelerator="Ctrl+A", command=seleccionar_todo)
barra_menu.add_cascade(menu=menu_edicion, label="Edición")

#Menú ver
menu_ver = tk.Menu(barra_menu, tearoff=False)
menu_ver.add_command(label="Color de fondo", command=fondo_color)
barra_menu.add_cascade(menu=menu_ver, label="Ver")

#Menú ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=False)
menu_ayuda.add_command(label="Ayuda", command=ayuda)
menu_ayuda.add_separator()
menu_ayuda.add_command(label="Acerca del Bloc de notas", command=acerca_programa)
barra_menu.add_cascade(menu=menu_ayuda, label="Ayuda")

root.config(menu=barra_menu)

#Barra de herramientas 1

#Funciones y variables
def pintar_imgs():
    imgs = {}
    for i in glob.glob("icons/*.png"):
        pathfile = i
        i = os.path.basename(i)
        name = i.split(".")[0]
        imgs[name] = PhotoImage(file=pathfile)
    return imgs

barra_herramientas_1 = tk.Frame(root)
barra_herramientas_1.pack(side=TOP, fill=X)
imgs = pintar_imgs()

#Botones de la barra de herramientas 1
def boton_herramientas_1(poner_comando, poner_imagen):
    boton = Button(
        barra_herramientas_1,
        relief=FLAT,
        compound=LEFT,
        command=poner_comando,
        image=imgs[poner_imagen]
        )
    boton.pack(side=LEFT, padx=0, pady=0)

b1 = boton_herramientas_1(nuevo, "nuevo-32")
b2 = boton_herramientas_1(abrir, "abrir-32")
b3 = boton_herramientas_1(guardar, "guardar-32")
b4 = boton_herramientas_1(cortar, "cortar-32")
b5 = boton_herramientas_1(copiar, "copiar-32")
b6 = boton_herramientas_1(pegar, "pegar-32")
b7 = boton_herramientas_1(deshacer, "deshacer-32")
b8 = boton_herramientas_1(rehacer, "rehacer-32")
b9 = boton_herramientas_1(fondo_color, "color-fondo-32")
b10 = boton_herramientas_1(buscar_reemplazar, "buscar-32")
b11 = boton_herramientas_1(ayuda, "ayuda-32")

#Barra de herramientas 2

#Tipo de fuente
fuente = list(font.families())

def tipo_fuente(event):
    global fuente_tipo
    fuente_tipo = variable_tipo.get()
    area_texto.config(font=(fuente_tipo,fuente_tamaño))

#Estilo de fuente
def texto_cursiva():
    propiedad_texto = font.Font(font=area_texto['font']).actual()
    if propiedad_texto['slant']=='roman':
        area_texto.config(font=(fuente_tipo,fuente_tamaño,'italic'))
    if propiedad_texto['slant']=='italic':
        area_texto.config(font=(fuente_tipo,fuente_tamaño,'roman'))

def texto_negrita():
    propiedad_texto = font.Font(font=area_texto['font']).actual()
    if propiedad_texto['weight']=='normal':
        area_texto.config(font=(fuente_tipo,fuente_tamaño,'bold'))
    if propiedad_texto['weight']=='bold':
        area_texto.config(font=(fuente_tipo,fuente_tamaño,'normal'))

def texto_subrayado():
    propiedad_texto = font.Font(font=area_texto['font']).actual()
    if propiedad_texto['underline']==0:
        area_texto.config(font=(fuente_tipo,fuente_tamaño,'underline'))
    if propiedad_texto['underline']==1:
        area_texto.config(font=(fuente_tipo,fuente_tamaño))

#Tamaño
tamaño = []

for i in range(8,73):
    tamaño.append(i)

def tamaño_fuente(event):
    global fuente_tamaño
    fuente_tamaño = variable_tamaño.get()
    area_texto.config(font=(fuente_tipo,fuente_tamaño))

#Color de texto
def texto_color():
    color = colorchooser.askcolor()[1]
    area_texto.config(fg= color, insertbackground = color)

#Variables de la barra de herramientas 2
barra_herramientas_2 = Label(root)
barra_herramientas_2.pack(side=TOP,fill=X)

#Combobox tipo y tamaño
tipos_fuentes = font.families()
variable_tipo = StringVar()
combobox_tipo = Combobox(barra_herramientas_2,values=fuente,textvariable=variable_tipo,state='readonly',width='20')
combobox_tipo.current(tipos_fuentes.index('Arial'))
combobox_tipo.pack(side=LEFT, padx=0, pady=0)

separador = Label(barra_herramientas_2,text=" ")
separador.pack(side=LEFT, padx=0, pady=0)

variable_tamaño=IntVar()
combobox_tamaño = Combobox(barra_herramientas_2,values=tamaño,textvariable=variable_tamaño,state='readonly',width='8')
combobox_tamaño.set('12')
combobox_tamaño.pack(side=LEFT, padx=0, pady=0)

combobox_tipo.bind('<<ComboboxSelected>>',tipo_fuente)
combobox_tamaño.bind('<<ComboboxSelected>>',tamaño_fuente)

#Botones de la barra de herramientas 2
separador = Label(barra_herramientas_2,text=" ")
separador.pack(side=LEFT, padx=0, pady=0)

def boton_herramientas_2(poner_comando, poner_imagen):
    boton = Button(
        barra_herramientas_2,
        relief=FLAT,
        compound=LEFT,
        command=poner_comando,
        image=imgs[poner_imagen]
        )
    boton.pack(side=LEFT, padx=0, pady=0)

b12 = boton_herramientas_2(texto_negrita, 'negrita-20')
b13 = boton_herramientas_2(texto_cursiva, 'cursiva-20')
b14 = boton_herramientas_2(texto_subrayado, 'subrayado-20')
b15 = boton_herramientas_2(texto_color, 'color-texto-20')

#Área de texto
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
area_texto = Text(root, yscrollcommand=scrollbar.set, undo=True)
area_texto.pack(fill="both", expand=1)
area_texto.config(bd=0, padx=6, pady=5, font=(fuente_tipo, fuente_tamaño))
scrollbar.config(command=area_texto.yview)
area_texto.bind('<<Modified>>', barra_estado)

#Menú contextual del área de texto
menu_contextual_texto = tk.Menu(tearoff=0)
menu_contextual_texto.add_command(label="Deshacer", command=deshacer)
menu_contextual_texto.add_command(label="Rehacer", command=rehacer)
menu_contextual_texto.add_separator()
menu_contextual_texto.add_command(label="Cortar", command=cortar)
menu_contextual_texto.add_command(label="Copiar", command=copiar)
menu_contextual_texto.add_command(label="Pegar", command=pegar)
menu_contextual_texto.add_command(label="Eliminar", command=eliminar)
menu_contextual_texto.add_separator()
menu_contextual_texto.add_command(label="Seleccionar todo", command=seleccionar_todo)

def hacer_contextual_texto(event):
    menu_contextual_texto.tk_popup(event.x_root, event.y_root)

#Si se usa mac os, por favor, cambiar a <Button-2>
root.bind("<Button-3>", hacer_contextual_texto)

#Teclas rápidas
root.bind("<Control-n>",nuevo)
root.bind("<Control-N>",nuevo)
root.bind("<Control-o>",abrir)
root.bind("<Control-O>",abrir)
root.bind("<Control-s>",guardar)
root.bind("<Control-S>",guardar)
root.bind("<Control-Alt-s>",guardar_como)
root.bind("<Control-Alt-S>",guardar_como)
root.bind("<Control-q>",salir)
root.bind("<Control-Q>",salir)
root.bind("<Control-f>",buscar_reemplazar)
root.bind("<Control-F>",buscar_reemplazar)

root.mainloop()