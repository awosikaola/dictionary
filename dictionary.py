import json

data = json.load(open("data.json", 'r'))

def meaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    else:
        print("This word doesn't exist, please check to confirm")

word = input('Enter the word you will like to search: ')

print(meaning(word))