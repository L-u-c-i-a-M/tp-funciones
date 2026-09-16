def precio_final_nombrada(precio, iva=0.21):
    return precio * (1 + iva)

precio_final_anonima = lambda precio, iva=0.21: precio * (1 + iva)

print("Precio final nombrado (100, IVA 21%):", precio_final_nombrada(100))
print("Precio final anónimo (100, IVA 21%):", precio_final_anonima(100))
print("Precio final nombrado (100, IVA 10%):", precio_final_nombrada(100, iva=0.10))
print("Precio final anónimo (100, IVA 10%):", precio_final_anonima(100, iva=0.10))
