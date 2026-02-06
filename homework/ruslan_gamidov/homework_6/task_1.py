text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
        ' dignissim vitae libero')

text_split = text.split()
new_text = []

for word in text_split:
    if ',' in word or '.' in word:
        new_text.append(word[:-1] + 'ing' + word[-1])
    else:
        new_text.append(word + 'ing')

print(' '.join(new_text))
