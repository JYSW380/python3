import json
# import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word.lower()in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "Word is not in the dictionary"

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


# print(SequenceMatcher(None, "rainn", "rain").ratio())
# print(get_close_matches("rajinn", ["help", "pyramind", "rain"]))

