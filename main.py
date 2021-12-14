# importing the module with all functions
import mod

'''main program import the above module to read the attached file
 ‘valleyoffear.txt’. The program should process the content of the file
  and find the 10 most used words in the file. Create a file called 
  ‘mostusedwords.txt’ and write these 10 most used words to this file.'''

# creates a variable that makes the valleyoffear text a string and stores as x

x = mod.text_string('valleyoffear.txt')

# most stores the top ten words in a list without the amount of words just the words themselves
most = mod.most_used(x)

# this writes that the most list into the mostusedwords.txt
mod.new_line('mostusedwords.txt', most)
