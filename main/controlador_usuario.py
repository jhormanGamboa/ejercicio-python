from modelo import modelo_e
from vista_formulario import vistaformulario
class controlador_formulario:
    def __init__(self,obmodelo,objvista) :
        self.objmodelo=obmodelo
        self.obvista=objvista

    def enviardatos(self):
        nombre = self.obvista.entry_nombre.get()
        apellido = self.obvista.entry_apellido.get()
        edad = self.obvista.entry_edad.get()
        correo = self.obvista.entry_correo.get()
        genero = self.obvista.entry_genero.get()

        datos = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "correo": correo,
            "genero": genero
        }

        self.objmodelo.escribir_json("datos.json", datos)
        self.obvista.lab_resultado.config(text="Datos enviados correctamente.")


obmodelo=modelo_e
obvista=vistaformulario()
obcontrolador=controlador_formulario(obmodelo,obvista)
obcontrolador.enviardatos()
obvista.crear_boton()


obvista.iniciar()


    
