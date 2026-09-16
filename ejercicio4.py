def convertir_nombrada(metros, unidad="cm"):
    if unidad == "cm":
        return metros * 100
    elif unidad == "mm":
        return metros * 1000
    else:
        raise ValueError("Unidad no soportada. Usar 'cm' o 'mm'.")

convertir_anonima = lambda metros, unidad="cm": metros * 100 if unidad == "cm" else metros * 1000

print("1 metro a cm (nombrado):", convertir_nombrada(1))
print("1 metro a mm (nombrado):", convertir_nombrada(1, unidad="mm"))
print("1 metro a cm (anónimo):", convertir_anonima(1))
print("1 metro a mm (anónimo):", convertir_anonima(1, unidad="mm"))
