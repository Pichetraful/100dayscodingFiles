# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
nato_alphabet_dict = {row["letter"]:row["code"] for (index, row) in nato_alphabet.iterrows()}
# print(nato_alphabet_dict)
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name_to_divide = input("Enter a word: ").upper()

name_to_alphabet = [nato_alphabet_dict[letter] for letter in name_to_divide]

print(name_to_alphabet)