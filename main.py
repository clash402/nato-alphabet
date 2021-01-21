import pandas


# PROPERTIES
PATH = "./nato_alphabet.csv"

df = pandas.read_csv(PATH)
nato_dict = {row.letter: row.code for index, row in df.iterrows()}


# METHODS
def generate_nato_alphabet():
    word = input("Enter a word: ").upper()

    try:
        words = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_nato_alphabet()
    else:
        words_str = " ".join(words)
        print(words_str)


# MAIN
generate_nato_alphabet()
