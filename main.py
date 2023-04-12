import csv

print('\n\n\n')
print('▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀ ██▓     ██▓  ██████ ▄▄▄█████▓    ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █  ')
print('▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒   ▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ ')
print('▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░   ▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒')
print('▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒██░    ░██░  ▒   ██▒░ ▓██▓ ░    ░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒')
print('▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░██████▒░██░▒██████▒▒  ▒██▒ ░     ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░')
print('░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░       ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ')
print('  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░         ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░')
print('░         ░  ░░ ░   ░   ░        ░ ░░ ░   ░ ░    ▒ ░░  ░  ░    ░           ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░      ░     ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ ')
print('░ ░       ░  ░  ░   ░  ░░ ░      ░  ░       ░  ░ ░        ░                    ░  ░   ░                  ░ ░         ░         ░  ░         ░      ░ ░           ░ ')
print('░                       ░                                                                                                                                          ')
print('\n\n\n')

words = {}

print('Enter a feature and write stop when you finish')


questions = {
    "w": "Does the {word} work properly?",
    "ww": "Do the {word} work correctly?",
    "d": "Is the {word} broken or damaged?",
    "dd": "Are the {word} broken or damaged?",
    "h": "Does the car have any {word}?",
    "f": "Does the car have {word} around it?",
}

word_lists = {
    "w": ["engine", "transmission", "brakes", "lights", "windows", "radio", "air conditioning", "heater", "defroster"],
    "d": ["engine", "transmission", "brakes", "lights", "windows", "mirrors", "body"],
    "h": ["scratches", "dents", "rust", "odor"],
    "f": ["people", "vehicles", "obstacles"],
}

words = []

while True:
    entrada = input("word: ")
    if entrada.lower() == "stop":
        break
    word = entrada.lower()
    tipo = None
    for t, lst in word_lists.items():
        if word in lst:
            tipo = t
            break
    if tipo is None:
        print("Word not recognized, skipping...")
    else:
        words.append((word, tipo))

with open("vehicles.csv", mode="w", newline="") as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["Question", "Answer Type", "Expected Answer", "Critical", "Exclude Random"])
    for word, tipo in words:
        if tipo == "d":
            question = "Is the {word} broken or damaged?"
        else:
            question = questions.get(tipo, "")
            question = question.format(word=word)
        expected_answer = "Y" if tipo in ("w", "h") else "N"
        writer.writerow([question, "Yes/No", expected_answer, "N", "N"])
