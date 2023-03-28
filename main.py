import csv

print("Chekclist automation")
print("")
print("Ing J.Luis Huergo")
print("")

words = {}

while True:
    # Solicitamos al usuario que ingrese la palabra y su tipo
    entrada = input("Enter a feature and its category (w, d, f): ")

     # Si el usuario decide salir, salimos del bucle infinito
    if entrada.lower() == "stop":
        break

    palabra, tipo = entrada.split()
    words[palabra] = tipo



with open("vehicles.csv", mode="w", newline="") as archivo_csv:
    # Creamos un objeto writer de CSV
    writer = csv.writer(archivo_csv)

    writer.writerow(["", "Type", "Expected Answer", "Critical","Exclude Random"])
    # Recorremos las palabras del diccionario y las clasificamos según su tipo
    for palabra, tipo in words.items():
        if tipo == "w":
            pregunta = f"Are the {palabra} working properly?"
        elif tipo == "d":
            pregunta = f"Is the {palabra} damage"
        elif tipo == "f":
            pregunta = f"Does the car have {palabra} around it ?"

        if tipo == "w":
            e = "Y"
        else:
            e = "N"

        expected_answer = e

        writer.writerow([pregunta, "Yes/No", expected_answer, "N", "N"])



