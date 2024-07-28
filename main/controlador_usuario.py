from vista_formulario import VistaFormulario
from modelo import modelo_e
class Controlador:
    def __init__(self, objvista, objmodelo):
        self.vista = objvista
        self.modelo = objmodelo

    def enviar_datos(self):
        datos = objvista.obtener_datos()

        # aco estoy validadndo la eda de que sea un numero entero
        if not self.validar_edad(datos["Edad"]):
            objvista.mostrar_mensaje("Error" " " "Rellena los campos correctamente")
            return
        
        # aca estoy actualizando los datos
        objmodelo.set_nombre(datos["Nombre"])
        objmodelo.set_apellido(datos["Apellido"])
        objmodelo.set_edad(datos["Edad"])
        objmodelo.set_correo(datos["Correo electronico"])
        objmodelo.set_genero(datos["Genero"])
        
        # aqui guardo los datos que envio
        objmodelo.archvonuevo(datos)
        objvista.mostrar_mensaje("Informacion" " ""Datos enviados correctamente")

    def validar_edad(self, edad_texto):
        try:
            int(edad_texto)
            return True
        except ValueError:
            return False
        
        

objvista = VistaFormulario()
objvista.crear_ventana()
objvista.crear_boton() 
objmodelo = modelo_e ()
objcontrolador = Controlador(objvista,objmodelo)
objvista.boton.config(command=objcontrolador.enviar_datos)    
objvista.iniciar()