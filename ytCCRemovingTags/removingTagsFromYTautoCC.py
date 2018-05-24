
import re
with open('ytAutoCC.txt', 'r') as f:
    file_contents = f.readlines()[1:]                           # Starts reading from the second line until the end. 
    f_contents_str = ''.join(file_contents)                     # Joins all the elements of the list to a string.
    f_contents_str_no_brackets = re.sub('<[^>]*>', ' ', f_contents_str)  # Replace brackets for spaces.
    f_contents_str_no_brackets2 = f_contents_str_no_brackets.replace('&#39;', "'")
    f_contents_list = f_contents_str_no_brackets2.split()       # Convert to list. Cleans up some left over spaces.
    f_contents_str_final = ' '.join(f_contents_list)

    with open("transcriptPure.txt", "w") as file_storing_object:
        file_storing_object.write(f_contents_str_final)
