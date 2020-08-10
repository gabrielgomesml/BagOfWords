# First step: Convert all strings to their lower case form

phrases = ['Hello, World!', 'Congratulations! You win. Win from home', 'Hi, how are you', 'Call me now!']

def lowerCase(string):
    return string.lower()

lowerCasePhrases = []
for sentences in phrases:
    lowerCasePhrases.append(lowerCase(sentences))

'''print(lowerCasePhrases)'''

# Second step: Removing all punctuations

phrasesWithoutPunctuations = []

def removePunctuations(string):
    newString = ''
    for letter in string:
        if ord(letter) >= 97 and ord(letter) <= 122 or letter == ' ':
            newString += letter
    return newString

for i in lowerCasePhrases:
    phrasesWithoutPunctuations.append(removePunctuations(i))

'''print(phrasesWithoutPunctuations)'''

# Thrid step: Tokenization (splitting up a sentence into individual words)

phrasesTokenized = []

for i in phrasesWithoutPunctuations:
    phrasesTokenized.append(i.split())

'''print(phrasesTokenized)'''

# Fourth step: Counting frequencies

frequencyList = []

for phrases in phrasesTokenized:
    aux = {}
    for words in phrases:
        if words not in aux:
            aux[words] = 1
        else:
            aux[words] += 1
    frequencyList.append(aux)

print(frequencyList)
