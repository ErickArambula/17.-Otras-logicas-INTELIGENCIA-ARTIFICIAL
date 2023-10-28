import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear las variables de entrada y salida difusas
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía
calidad.automf(3)
servicio.automf(3)
propina['bajo'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['medio'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alto'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Crear reglas difusas
regla1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
regla2 = ctrl.Rule(service['average'], tip['medium'])
regla3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])

# Crear el simulador difuso
simulador = ctrl.ControlSystemSimulation(sistema_control)

# Ingresar valores a las variables de entrada
simulador.input['calidad'] = 6.5
simulador.input['servicio'] = 9.8

# Realizar la inferencia
simulador.compute()

# Obtener el resultado
print("Valor de la propina:", simulador.output['propina'])
