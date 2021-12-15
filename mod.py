# Function 1: take a file name as an input.
# Read the file and store the contents of the file in a string then return a string.

def text_string(file_name):  # input is file name
    # opening the file in read mode
    # replace r with encoding='utf8' if everything else fails
    words = open(file_name, 'r')
    # creating a variable that contains the string
    r = words.read()
    words.close()
    return r  # returns the string


# Function 2: take a string as an input, reads the string and finds the 10
# most used words in the string. It will return the list of 10 most used words.
def most_used(words):
    # new dictionary to store how many times that word happens
    d_words = {}
    # list is going to be the return value.
    word_list = words.split() # this splits the text into a list
    # this for loop counts the amount of times the same word
    # comes up throughout the text
    for char in word_list:
        if char in d_words.keys():
            # if the word is already in add one to that keys value
            d_words[char] += 1
        else:
            # else makes a new key with the value of 1
            d_words[char] = 1
    # this pretty much make a tupple out of keys and values
    # the format of them are (value, key) this is, so I can sort the list
    # This is all compiled by using list comprehension
    most_list = [(val, key) for key, val in d_words.items()]
    # sorted so that it is biggest to smallest
    sort = sorted(most_list, reverse=True)
    # then is put into a list with only the words and not the number of times it was repeated
    just_words = [i[1] for i in sort]
    # returns the first ten elements in the list
    return just_words[:10]

# Function 3: take a file name and a list of words as input.
# Creates a file with the file name and writes  the list of words to the file.
# Each word to be on a new line. The function will not return anything.

def new_line(file_name, list):
    # I wanted to diversify how I opened the file also this one
    # has automatic closing this is from what
    # I learned from zybooks I wanted to try it out see how it worked

    with open(file_name, 'w') as file:
        # this list comprehension writes the words in the list to the
        # mostusedwords.txt file
        [file.write(str(i) + '\n') for i in list]

