
class modelo_e:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.correo = None
        self.genero = None

    def get_nombre(self):
       return self.nombre
    
    def get_apellido(self):
       return self.apellido
    
    def get_edad(self):
       return self.edad
    
    def get_correo(self):
       return self.correo
    
    def get_genero(self):
       return self.genero
    
    def set_nombre(self,datonombre):
       self.nombre = datonombre

    def set_apellido(self,datoapellido):
       self.apellido = datoapellido
   
    def set_edad(self,datoedad):
       self.edad = datoedad
      
    def set_correo(self,datocorreo):
       self.correo = datocorreo

    def set_genero(self,datogenero):
       self.genero = datogenero
    
    def formato_texto(self):
       return f"{self.get_nombre()}, {self.get_apellido()}, {self.get_edad()}, {self.get_correo()}, {self.get_genero()}"
                   
    def guardar_archivo(self,archivo="archivo.txt"):
       datos = self.formato_texto()
       with open(archivo,"a") as linea:
          linea.write(datos + "\n")
    
    