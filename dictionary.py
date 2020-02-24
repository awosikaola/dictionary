import json
#help(json.load)

data = json.load(open("data.json", 'r'))

def meaning(word):
    return data[word]

word = input('Enter the word you will like to search: ')

print(meaning(word))