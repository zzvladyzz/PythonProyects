
#SUPERCLASE
class Usuarios():    
    Tipo_Usuario="Free"
    Precio=10
    def __init__(self,Nombre,DNI):
        self.Nombre=Nombre
        self.DNI=str(DNI)
        self.Juegos=[]

    def Datos_Usuario(self):
        print("El nombre de usuario es:",self.Nombre)
        print("\tSu DNI es:",self.DNI)
        print("\tSus Juegos son:",self.Juegos)


#SUBCLASE                        #SuperClase
class Usuarios_Premiun(Usuarios):
    
    Tipo_Usuario="Premiun"
    
    Precio=20

    def __init__(self,Nombre,DNI,Participacion_Sorteos):
        #Usuarios.__init__(self,Nombre,DNI)
        super().__init__(Nombre,DNI)
        self.Participacion_Sorteos=int(Participacion_Sorteos)

    def Datos_Usuario(self):
        Usuarios.Datos_Usuario(self)    
        print("\tLa Participacion en sorteos es de= ",self.Participacion_Sorteos)
        print("\tSu precio a pagar es= ",self.Precio)
        


                                #SubClase
class Usuarios_Premiun_Plus(Usuarios_Premiun):
    Precio=30
    def Datos_Usuario(self):
        #Usuarios_Premiun.Datos_Usuario(self)
        super().Datos_Usuario()
        print("\tEl tipo de usuario es: "+self.Tipo_Usuario)


Usuario1=Usuarios("Vlady",5520)
Usuario2=Usuarios_Premiun("Dania",2545,22)
Usuario3=Usuarios_Premiun_Plus("Victor",5423,30)
juegos=['I Bread','Matrix','COD WW2','Fortnite']
Usuario3.Juegos.append(juegos)
Usuario3.Juegos.append('Read dead Redention')

Usuario1.Datos_Usuario()
Usuario2.Datos_Usuario()
Usuario3.Datos_Usuario()
