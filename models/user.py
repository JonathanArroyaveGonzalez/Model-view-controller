class UserModel:
    def __init__(self,nombre,apellido,profesion):
        self.nombre=nombre,
        self.apellido=apellido,
        self.profesion=profesion,
    def viewUserData(self):
        return {"Nombre":self.nombre,
                "Apellido": self.apellido,
                "Profesion":self.profesion}