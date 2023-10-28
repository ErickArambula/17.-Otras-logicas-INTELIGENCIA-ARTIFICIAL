from pyknow import Fact, Rule, KnowledgeEngine

class MiMotor(KnowledgeEngine):
    @Rule(Fact(cielo="nublado"))
    def conclusion1(self):
        self.declare(Fact(lluvia="probable"))

    @Rule(Fact(lluvia="probable"), Fact(fuerte_viento=True))
    def conclusion2(self):
        self.declare(Fact(lluvia="improbable"))

    @Rule(Fact(lluvia="improbable"))
    def conclusion3(self):
        self.declare(Fact(cielo="despejado"))

# Crear una instancia del motor
motor = MiMotor()

# Insertar un hecho inicial
motor.declare(Fact(cielo="nublado"))

# Ejecutar el motor de inferencia
motor.run()

# Obtener conclusiones
conclusiones = list(motor.facts)

for hecho in conclusiones:
    print(hecho)
