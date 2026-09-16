def area_nombrada(base, altura=None):
    if altura is None:
        altura = base
    return base * altura

area_anonima = lambda base, altura=None: base * (altura if altura is not None else base)

print("Área rectángulo nombrado (base=5, altura=3):", area_nombrada(5, 3))
print("Área cuadrado nombrado (base=5):", area_nombrada(5))
print("Área rectángulo anónimo (base=5, altura=3):", area_anonima(5, 3))
print("Área cuadrado anónimo (base=5):", area_anonima(5))
