class Carro():
    def __init__(self,placa=None,marca=None,modelo=None,color=None):
        self.__placa=placa
        self.marca=marca
        self.__modelo=modelo
        self.color=color        
        
    def getPlaca(self):
        return self.__placa
    
    def getModelo(self):
        return self.__modelo
    
    def setPlaca(self,placa):
        self.__placa=placa
        
    def setModelo(self,modelo):
        self.__modelo=modelo
  
  
carro = Carro("qqq123","Mazda",2010,"Rojo")

otroCarro= Carro(modelo=2000)  

print(carro.getPlaca(), carro.marca, carro.getModelo(), carro.color)

class Libro:
    def __init__(self,titulo=None,autor=None,numeroPaginas=None) -> None:
        self.__titulo=titulo
        self.__autor=autor
        self.__numeroPaginas=numeroPaginas

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getNumeroPaginas(self):
        return self.__numeroPaginas
    
    def setTitulo(self,titulo):
        self.__titulo=titulo
        
    def setAutor(self,autor):
        self.__autor=autor
        
    def setNumeroPaginas(self,numeroPaginas):
        self.__numeroPaginas=numeroPaginas
          
libro = Libro("El Principito","Antoine de Saint",500)

otroLibro= Libro(titulo=2000)  

print(libro.getTitulo(), libro.getAutor(), libro.getNumeroPaginas())




