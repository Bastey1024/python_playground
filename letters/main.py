name_list=[]
with open ("Input/Names/invited_names.txt") as names:
    for line in names:
        name_list.append(line)

for name in name_list:
    with open ("Input/Letters/starting_letter.txt") as letter:
        changed_letter=letter.read().replace("[name]",name)
        new_file=open(f"Output/ReadyToSend/letter_for_{name[0:len(name)-1]}.txt",'w')
        new_file.write(changed_letter)
        new_file.close()



#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
