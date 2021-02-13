
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")

dictionary =  {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    sentence = input("Type in your stuff : ")

    try:
        output= [dictionary[letter.upper()] for letter in sentence]
    except KeyError:
        print("Sorry only Alphabeticalletter")
        generate_phonetic()

    else:
        print(output)



generate_phonetic()
