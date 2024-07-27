import tkinter as tk
from tkinter import messagebox

class vistaformulario:
    def __init__(self):
        self.ventana = None

    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de formulario")
        self.ventana.geometry("500x500")
        self.ventana.config(bg="#96BEDB", highlightbackground="#7cfda3", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#D3D3D3", highlightbackground="#5C8B9A", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=270, height=450)
        
        self.label_nombre = tk.Label(self.contenedor, text="Ingrese su nombre: ", bg="#DFEDF6")
        self.label_nombre.pack(pady=5, padx=5, anchor='center')
        self.entry_nombre = tk.Entry(self.contenedor)
        self.entry_nombre.pack(pady=5, padx=5)
        
        self.label_apellido = tk.Label(self.contenedor,text="Ingrese el apellido: ", bg="#DFEDF6")
        self.label_apellido.pack(pady=5, padx=5, anchor='center')
        self.entry_apellido = tk.Entry(self.contenedor)
        self.entry_apellido.pack(pady=5,padx=5)
        
        self.label_edad = tk.Label(self.contenedor,text="Ingrese la edad: ", bg="#DFEDF6")
        self.label_edad.pack(pady=5, padx=5, anchor='center')
        self.entry_edad = tk.Entry(self.contenedor)
        self.entry_edad.pack(pady=5,padx=5)
        
        self.label_correo = tk.Label(self.contenedor,text="Ingrese el correo electronico: ", bg="#DFEDF6")
        self.label_correo.pack(pady=5, padx=5, anchor='center')
        self.entry_correo = tk.Entry(self.contenedor)
        self.entry_correo.pack(pady=5,padx=5)
        
        self.label_genero = tk.Label(self.contenedor,text="Ingrese el genero: ", bg="#DFEDF6")
        self.label_genero.pack(pady=5, padx=5, anchor='center')
        self.entry_genero = tk.Entry(self.contenedor)
        self.entry_genero.pack(pady=5,padx=5)

    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Enviar datos")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#DFEDF6")
        self.label_resultado.pack(pady=10)
    
    def validar_edad(self):
        edad_texto = self.entry_edad.get()
        try:
            edad = int(edad_texto)
            self.label_resultado.config(text="Datos enviado correctamente.", fg="green")
        except ValueError:
            self.label_resultado.config(text="Error la edad debe de ser un numero entero.", bg="red") 

    def incion(self):
        self.ventana.mainloop()        

   