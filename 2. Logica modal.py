from modal_logic_parser import Formula

# Crear una fórmula modal
formula = Formula("◇P -> ¬◻Q")

# Evaluar la fórmula en un modelo posible
modelo = {"P": True, "Q": False}
cumple = formula.evaluate(modelo)

print("La fórmula se cumple en este modelo:", cumple)
