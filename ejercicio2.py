def resta_nombrada(*, num1, num2):
    return num1 - num2

resta_anonima = lambda num1, num2: num1 - num2

print("Resta nombrada (10 - 3):", resta_nombrada(num1=10, num2=3))
print("Resta anónima (10 - 3):", resta_anonima(10, 3))
