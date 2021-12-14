import mod

'''main program import the above module to read the attached file
 ‘valleyoffear.txt’. The program should process the content of the file
  and find the 10 most used words in the file. Create a file called 
  ‘mostusedwords.txt’ and write these 10 most used words to this file.'''

x = mod.text_string('valleyoffear.txt')
most = mod.most_used(x)
print(most)

mod.new_line('mostusedwords.txt', most)