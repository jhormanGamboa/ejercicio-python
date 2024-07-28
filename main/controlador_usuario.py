import json
from vista_formulario import VistaFormulario
from modelo import modelo_e
class Controlador:
    def __init__(self, objvista, objmodelo):
        self.objvista = objvista
        self.objmodelo = objmodelo

    def enviar_datos(self):
        datos = self.objvista.obtener_datos()

        # aco estoy validadndo la eda de que sea un numero entero
        if not self.validar_edad(datos["Edad"]):
            self.objvista.mostrar_mensaje("Error" " " "Rellena los campos correctamente")
            return
        
        # aca estoy actualizando los datos
        self.objmodelo.set_nombre(datos["Nombre"])
        self.objmodelo.set_apellido(datos["Apellido"])
        self.objmodelo.set_edad(datos["Edad"])
        self.objmodelo.set_correo(datos["Correo electronico"])
        self.objmodelo.set_genero(datos["Genero"])
        
        # aqui guardo los datos que envio
        self.objmodelo.guardar_archivo()
        self.objvista.mostrar_mensaje("Informacion" " ""Datos enviados correctamente")

    def validar_edad(self, edad_texto):
        try:
            int(edad_texto)
            return True
        except ValueError:
            return False
        
    def procesojson(self):
      with open("archivo.txt","r") as archivo:
       auxdato= archivo.readlines()
       return [json.loads(linea.strip()) for linea in auxdato]
    
    


        
        

objvista = VistaFormulario()
objmodelo = modelo_e ()
objcontrolador = Controlador(objvista,objmodelo)
objvista.crear_ventana()
objvista.crear_boton() 
objvista.crear_boton2()
objvista.boton.config(command=objcontrolador.enviar_datos)    
objvista.boton_borrar.config(command=objvista.borrar_datos)
objvista.iniciar()