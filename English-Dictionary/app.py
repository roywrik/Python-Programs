import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if yn.upper() == "Y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn.upper == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "Please enter valid query."
    else:
        return "The word doesn't exist. Please double check it."

user = input("Enter word: ")

output = translate(user)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)