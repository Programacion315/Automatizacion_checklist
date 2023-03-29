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

print('Enter a feature and its category (w, d, f, h): working - damage - fluids - have')
print('\n')
print('Formats')
print('w - Does the _____ work properly?')
print('d - Is the _____ broken or damage?')
print('h - Does the car have any _____?')
print('f - Does the car have _____ around it?')
print('\n')


import csv

questions = {
    "w": "Does the {word} work properly?",
    "ww": "Do the {word} work correctly?",
    "d": "Is the {word} broken or damaged?",
    "dd": "Are the {word} broken or damaged?",
    "h": "Does the car have any {word}?",
    "f": "Does the car have {word} around it?",
}

words = {}

while True:
    entrada = input("word: ")
    if entrada.lower() == "stop":
        break
    word, tipo = entrada.split()
    words[word] = tipo

with open("vehicles.csv", mode="w", newline="") as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["Question", "Answer Type", "Expected Answer", "Critical", "Exclude Random"])
    for word, tipo in words.items():
        question = questions.get(tipo, "")
        question = question.format(word=word)
        expected_answer = "Y" if tipo in ("w", "h") else "N"
        writer.writerow([question, "Yes/No", expected_answer, "N", "N"])
