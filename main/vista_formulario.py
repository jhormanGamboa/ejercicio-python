import tkinter as tk

class vista_formulario:
    def __init__(self):
        self.ventana = None

    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de formulario")
        self.ventana.geometry("500x500")
        self.ventana.config(bg="#5dfc8a", highlightbackground="#7cfda3", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#9cfebc", highlightbackground="#64da58", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=270, height=450)
        
        self.label_nombre = tk.Label(self.contenedor, text="Ingrese su nombre: ", bg="#bbffd5")
        self.label_nombre.pack(pady=5, padx=5, anchor='center')
        self.entry_nombre = tk.Entry(self.contenedor)
        self.entry_nombre.pack(pady=5, padx=5)
        
        self.label_apellido = tk.Label(self.contenedor,text="Ingrese el apellido: ", bg="#bbffd5")
        self.label_apellido.pack(pady=5, padx=5, anchor='center')
        self.entry_apellido = tk.Entry(self.contenedor)
        self.entry_apellido.pack(pady=5,padx=5)
        
        self.label_edad = tk.Label(self.contenedor,text="Ingrese la edad: ", bg="#bbffd5")
        self.label_edad.pack(pady=5, padx=5, anchor='center')
        self.entry_edad = tk.Entry(self.contenedor)
        self.entry_edad.pack(pady=5,padx=5)
        
        self.label_correo = tk.Label(self.contenedor,text="Ingrese el correo electronico: ", bg="#bbffd5")
        self.label_correo.pack(pady=5, padx=5, anchor='center')
        self.entry_correo = tk.Entry(self.contenedor)
        self.entry_correo.pack(pady=5,padx=5)
        
        self.label_genero = tk.Label(self.contenedor,text="Ingrese el genero: ", bg="#bbffd5")
        self.label_genero.pack(pady=5, padx=5, anchor='center')
        self.entry_genero = tk.Entry(self.contenedor)
        self.entry_genero.pack(pady=5,padx=5)

    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Enviar datos")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#bbffd5")
        self.label_resultado.pack(pady=10)

    def iniciar(self):
        self.ventana.mainloop()

objvista = vista_formulario()
objvista.crear_ventana()
objvista.crear_boton()
objvista.iniciar()