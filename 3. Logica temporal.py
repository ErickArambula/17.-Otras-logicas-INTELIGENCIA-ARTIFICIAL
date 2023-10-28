from temporal_logic_parser import LTL

# Crear una fórmula LTL (Temporal Logic Formula)
formula = LTL.parse("F(G(P && Q))")

# Definir una secuencia de tiempo
secuencia_tiempo = [
    {"P": True, "Q": True},
    {"P": True, "Q": False},
    {"P": False, "Q": True},
    {"P": False, "Q": False}
]

# Evaluar la fórmula en la secuencia de tiempo
cumple = formula.holds(secuencia_tiempo)

print("La fórmula se cumple en la secuencia de tiempo:", cumple)
