import re

text = input()
search_word = input()
matching_words = []
pattern = rf"\b{search_word}\b"

answer = re.findall(pattern, text, re.IGNORECASE)
print(len(answer))
