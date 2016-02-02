'''word_or_phrase = input("Enter your choice of word(s): ")
word_or_phrase = word_or_phrase.split()
pig_latin_word = []
print(word_or_phrase)

for word in word_or_phrase:

    if word[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        pig_latin_word.append(word[1:] + "say")
    else:
        pig_latin_word.append(word[1:] + word[0] + "ay")

new_sentence = ' '.join(pig_latin_word)
print(new_sentence)'''


pig_latin_phrase = "illway erehay hetay milysay" #will here the emily
pig_latin_phrase = pig_latin_phrase.split()
english_word = []
print(pig_latin_phrase)

for word in pig_latin_phrase:

    if word[-3].lower() in ['s']:
        english_word.append("'A/E/I/O/U'" +  "-" + word[0:-3])

    else:
        english_word.append(word[-3].upper() + word[0:-3])

new_english_sentence = ' '.join(english_word)
print(new_english_sentence)