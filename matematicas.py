import math

# Solicitar al usuario los lados
a = float(input("Ingrese el lado a del triángulo: "))
b = float(input("Ingrese el lado b del triángulo: "))
c = float(input("Ingrese el lado c del triángulo: "))


# Función para calcular el ángulo en grados usando la ley de los cosenos
def calcular_angulo(a, b, c):
    cos_angulo = (a**2 + b**2 - c**2) / (2 * a * b)
    angulo_rad = math.acos(cos_angulo)
    return math.degrees(angulo_rad)

# Función principal para clasificar el triángulo y calcular sus ángulos
def caracterizar_triangulo(a, b, c):
    # Clasificación por lados
    if a == b == c:
        tipo_lados = "Equilátero"
    elif a == b or b == c or a == c:
        tipo_lados = "Isósceles"
    else:
        tipo_lados = "Escaleno"
    
    # Calcular los ángulos
    angulo_A = calcular_angulo(b, c, a)
    angulo_B = calcular_angulo(a, c, b)
    angulo_C = calcular_angulo(a, b, c)
    
    # Clasificación por ángulos
    if angulo_A == 90 or angulo_B == 90 or angulo_C == 90:
        tipo_angulo = "Rectángulo"
    elif angulo_A > 90 or angulo_B > 90 or angulo_C > 90:
        tipo_angulo = "Obtuso"
    else:
        tipo_angulo = "Acutángulo"
    
    # Mostrar resultados
    print(f"Triángulo de tipo {tipo_lados} y {tipo_angulo}.")
    print(f"Lados: a = {a}, b = {b}, c = {c}")
    print(f"Ángulos: A = {angulo_A:.2f}°, B = {angulo_B:.2f}°, C = {angulo_C:.2f}°")


# Llamar a la función para caracterizar el triángulo
caracterizar_triangulo(a, b, c)