banned_words = input().split(", ")
text = input()

for el in banned_words:
    if el in text:
        text = text.replace(el, "*" * len(el))

print(text)