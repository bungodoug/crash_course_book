# location of the little woman text
filename = "/Users/douglassmith/Documents/crashcourse material/little_women_sample.txt"

book_text = ""

with open(filename) as file_object:
    for line in file_object:
        try:
            line = line.strip()
            first_char = line[0]
            if first_char.isalpha() or first_char == '"':
                book_text += " " + line
        except IndexError:
            pass
        else:
            pass

unique_words = []
all_words = book_text.split(" ")

# print (all_words)

pre_processed_words = []

# may revisit below to define a list of non aplhas that i would
# like to treat as alphas ... such as ' (contraction) or - (hyphen)

for word in all_words:
    parsed_word = ""
    for character in word:
        if character.isalpha():
            parsed_word += character
    pre_processed_words.append(parsed_word)

# print(pre_processed_words)

word_count = {}

for word in pre_processed_words:
    word = word.lower()
    if word not in unique_words:
        kv_pair = {word: 1}
        word_count.update(kv_pair)
        unique_words.append(word.lower())
    else:
        word_score = word_count.get(word)
        # print(word_score)
        word_score += 1
        # print(word_score)
        kv_pair = {word: word_score}
        word_count.update(kv_pair)

# print(len(all_words))
# print(len(pre_processed_words))
# print(len(unique_words))
# print(word_count)

# list out keys and values separately
key_list = list(word_count.keys())
val_list = list(word_count.values())

print((val_list))
sorted_val_list = val_list.sort(reverse=True)
print((sorted_val_list))

dict_word_count = sum(word_count.values()) #how many words used in total
print(dict_word_count,"unique words have been used in the text supplied")
parito_breakpoint = 0.7 # how much of population to further refine
parito_target = dict_word_count * parito_breakpoint
parito_count = 0
index = 0
while parito_count <= parito_target:
    parito_count += val_list[index]
    index += 1

print(index, "words account for", parito_breakpoint*100,"% of word occurrences")

parito_key_list = key_list[0:index]
parito_val_list = val_list[0:index]

print(parito_key_list)
print(parito_val_list)

# this is someone else's code ... will look at it to see what i can
# learn ... but will try pandas approach first.

# import pandas as pd

import pandas as pd

# Calling DataFrame constructor after zipping
# both lists, with columns specified
# to view this dataframe from within pycharm, need to insert
# a breakpoint after the df has been created and before displayed
# run code in debugger mode, when code breaks, you can then right click
# on the df variable name and select "view as dataframe" either from RHS
# or from context menu.

df = pd.DataFrame(list(zip(parito_key_list, parito_val_list)),
                  columns=['Word', 'Cnt'])

df


# '''
# Get a list of keys from dictionary which has the given value
# '''
#
#
# def getKeysByValue(dictOfElements, valueToFind):
#     listOfKeys = list()
#     listOfItems = dictOfElements.items()
#     for item in listOfItems:
#         if item[1] == valueToFind:
#             listOfKeys.append(item[0])
#     return listOfKeys
#
# for top_words in range(0,max_word_plot):
#     frequency_target = val_list[top_words]
#     listOfKeys = getKeysByValue(word_count,frequency_target )
#     print("Keys with value equal to :",frequency_target)
#     # Iterate over the list of keys
#     for key in listOfKeys:
#         print(key)


#
# high_word_count = max(word_count.values())
# print (high_word_count)
# hi_word = word_count.get(high_word_count)
# print(hi_word)

# print(dict_word_count)

# import matplotlib.pyplot as plt
#
# plt.bar(range(len(word_count)), list(word_count.values()), align='center')
# plt.xticks(range(len(word_count)), list(word_count.keys()))
# # plt.show()
# plt.savefig("little_women.png")
