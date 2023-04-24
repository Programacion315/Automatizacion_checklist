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


import csv

print('Enter a feature and write stop when you finish')

questions = {
    "a": "Is this {word} safe to operate? -y",
    "b": "Is the {word} working? -y",
    "c": "Are the {word} working?",
    "d": "Is {word} readable and correct? -y",
    "e": "Are the {word} broken? -n",
}

word_lists = {
    "a": ["equipment"],
    "b": ["horn",],
    "c": ["lights",'beepers'],
    "d": ['data plate'],
    "e": ['mirrors'],
}

questions_csv = []

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
        parts = questions[tipo].format(word=word).split('-')
        question = parts[0]
        expected_answer = parts[1]
        questions_csv.append([question, "Yes/No", expected_answer.upper(), 'N', 'N'])

if questions_csv:
    with open('questions.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Answer Type', 'Expected Answer', 'Critical', 'Exclude Random'])
        writer.writerows(questions_csv)
    print("Questions saved to 'questions.csv'")
else:
    print("No questions entered.")


