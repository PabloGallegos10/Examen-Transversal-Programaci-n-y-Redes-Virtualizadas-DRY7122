as_number = int(input("Ingrese el número de AS de BGP: "))

if 64512 <= as_number <= 65534:
    print(f"El AS {as_number} es un AS privado.")
else:
    print(f"El AS {as_number} es un AS público.")
