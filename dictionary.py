import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

def meaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input ("Did you mean %s instead? If you mean Yes enter Y enter N for No: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Sorry the word doesn't exist"
    else:
        print("This word doesn't exist, please check to confirm")

word = input('Enter the word you will like to search: ')

print(meaning(word))