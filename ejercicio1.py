def suma_nombrada(num1, num2):
    return num1 + num2
suma_anonima = lambda num1, num2: num1 + num2
print("Resultado 1:", suma_nombrada(5, 10))
print("Resultado 2:", suma_anonima(7, 3))