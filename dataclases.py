from dataclasses import dataclass, field, asdict

@dataclass(frozen=True)

class Persona:
    nombre : str
    edad: int =field(default=35)

    def retornar_edad_por_2(self) -> int:
        return self.edad *2

@dataclass
class Puesto:
    nombre : str
    persona : Persona
class Persona2:
    def ___init__(self, nombre, edad= 35):
        self.nombre = nombre
        self.edad =edad


persona1 = Persona('Juan', 36)
persona2 = Persona('Camila')

puesto1 = Puesto('Desarrollador' , persona1)
print(puesto1)

print(asdict(persona1))

if persona1 == persona2:
    print('son iguales')
else:
    print('no son iguales')

