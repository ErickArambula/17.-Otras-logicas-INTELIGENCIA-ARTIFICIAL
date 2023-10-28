from defeasible import Argument, Fact, Rule, KB

# Definir hechos y reglas
hechos = [Fact("Pájaros_pueden_volar")]
reglas = [
    Rule(conditions=[Fact("Pájaros_pueden_volar")], conclusions=[Fact("Pájaros_vuelan", "defeasible")]),
    Rule(conditions=[Fact("Pájaros_vuelan")], conclusions=[Fact("Animales_vuelan", "defeasible")]),
]

# Crear una base de conocimiento
kb = KB(hechos, reglas)

# Evaluar un argumento
argumento = Argument(conditions=[Fact("Animales_vuelan")], conclusion=Fact("Animales_vuelan_vaga"))
conclusión = kb.evaluate(argumento)

print("Conclusión del argumento:", conclusión.value)
print("Justificación de la conclusión:", conclusión.justification)
