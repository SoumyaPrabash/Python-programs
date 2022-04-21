# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt') as invitation:
    contents = invitation.read()
with open('./Input/Names/invited_names.txt') as list_of_names:
    name_list = list_of_names.readlines()
    print(name_list)
    for name in name_list:
        file_name = name.rstrip()
        print(file_name)
        replaced_content = contents.replace("[name]", file_name)
        # with open(f"./Output/ReadyToSend/letter_for_{file_name}.txt", mode="w") as invitation:
        #     invitation.write(f"{replaced_content}")
