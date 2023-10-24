class Curso():
    
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__alumnos=[]
        
    def getNombre(self):
        return self.__nombre
    
    def getAlumnos(self):
        return self.__alumnos
        
    def matricularAlumno(self,alumno):
        self.__alumnos.append(alumno)
        
    def __str__(self):
        return self.__nombre
    
    def __del__(self):
        print("Eliminado curso")
        
class Alumno():
    
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def getEdad(self):
        return self.__edad
    
    def setEdad(self,edad):
        self.__edad=edad
        
    def __str__(self):
        return self.__nombre
        
unCurso = Curso("Python Avanzado")

alumno1 = Alumno("Maria",25)
alumno2 = Alumno("JUan",28)
alumno3 = Alumno("Rosa",18)

unCurso.matricularAlumno(alumno1)
unCurso.matricularAlumno(alumno2)

for alumno in unCurso.getAlumnos():
    print(alumno)
    
unCurso.__del__()

print(unCurso.getNombre())

print(alumno1)  