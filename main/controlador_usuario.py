from vista_formulario import VistaFormulario
from modelo import modelo_e
class Controlador:
    def __init__(self, objvista, objmodelo):
        self.vista = objvista
        self.modelo = objmodelo

        
        objvista.boton.config(command=self.enviar_datos)

    def enviar_datos(self):
        datos = objvista.obtener_datos()

        # aco estoy validadndo la eda de que sea un numero entero
        if not self.validar_edad(datos["edad"]):
            objvista.actualizar_resultado("Error: La edad debe ser un número entero.", "red")
            return
        
        
        # aca estoy actualizando los datos
        objmodelo.set_nombre(datos["nombre"])
        objmodelo.set_apellido(datos["apellido"])
        objmodelo.set_edad(datos["edad"])
        objmodelo.set_correo(datos["correo"])
        objmodelo.set_genero(datos["genero"])
        
        # aqui guardo los datos que envio
        objmodelo.archvonuevo(datos)
        objvista.actualizar_resultado("Datos enviados correctamente.", "green")

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
    
objvista.iniciar()

