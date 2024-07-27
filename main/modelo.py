import json
class modelo_e:
    def __init__(self):
        pass

    def procesojson(self):
      with open("archivo.txt","r") as archivo:
       auxdato=archivo.readlines()
       archivo.close()
       return auxdato
      
    def  cadena(self):
       with open("archivo.txt","w") as archivo:
          archivo.close
       
    def archivocrear(self):
       with open("sasas","w")as archivotexto:
          archivotexto.write()
          mensaje="Docemento creado"
          archivotexto.close()
          return mensaje
    def archvonuevo(self,datos):
       with open("archivo.txt", "w") as archivo:
          json.dump(datos,archivo)
