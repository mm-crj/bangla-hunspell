# Script to generate word frequency lists from the corpus
from inltk.inltk import setup
from inltk.inltk import tokenize
from inltk.inltk import remove_foreign_languages
from collections import Counter
import csv
import re

file_path='./txt/ekei-ki-bole-sobbhota.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

text = re.sub(r'[^\u0980-\u09FF\s]', '', text)

tokens = tokenize(text, 'bn')
token_frequency = Counter(tokens)

sorted_token_frequency = dict(sorted(token_frequency.items(), key=lambda item: item[1], reverse=True))

csv_file_path = 'token_frequency.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Token', 'Frequency'])

    for token, frequency in sorted_token_frequency.items():
        writer.writerow([token, frequency])

print(f'Token frequency saved to {csv_file_path}')
