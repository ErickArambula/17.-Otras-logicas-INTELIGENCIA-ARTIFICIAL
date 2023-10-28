from sympy import symbols, ForAll, Implies, And

# Definir variables y predicados
x, y = symbols('x y')
P = symbols('P', cls=Function)(x)
Q = symbols('Q', cls=Function)(x)

# Crear una fórmula de lógica de orden superior
formula = ForAll(x, Implies(P, Q))

# Evaluar la fórmula con un valor concreto
valor = And(P.subs(x, True), Q.subs(x, True))

# Comprobar si la fórmula se cumple con el valor dado
cumple = formula.subs(valor)
print("La fórmula se cumple con el valor dado:", cumple)
