def triangle_area(base, height):
    return (base * height) / 2

print("Calculadora de área de triángulo")
b = float(input("Base: "))
h = float(input("Altura: "))

area = triangle_area(b, h)
print(f"El área del triángulo es {area}")