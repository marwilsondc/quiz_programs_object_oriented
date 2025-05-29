#import pathlib
import pathlib 

#import Questions
from classes.Questions import Questions

#import Choices
from classes.Choices import Choices

#import Corrects
from classes.Corrects import Corrects

#import FilePath
from classes.FilePath import FilePath

#initialize current_path 
current_path = FilePath("questions.txt")

#define change_path for changing file being accessed
def change_path(new_file: str):
    global current_path
    current_path = FilePath(new_file)

def ques_count():
    with open(current_path, "r") as file:
        content = file.read()
        return content.count("<question>")
    file.close()

#while loop to continue asking user for input until ended
while True:
    ques_count()  
    ques_dict = {}

    #construct list of questions with ques_dict using block below
    with open(current_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "<question>" in line:
                if line not in ques_dict:
                    unclean_code = line.split(":")
                    clean_code = unclean_code[0].split(" ")
                    insert_code = clean_code[0]
                    ques_dict[insert_code] = Questions(unclean_code[1], unclean_code[0])


    local_count = ques_count()
    local_path_var = current_path

    #Main menu for the program, where the user will select from options
    print(f"""Welcome to Quiz Creator! 

Main Menu:
          
File opened: {local_path_var}

Questions added: {local_count} 
[1] Add Question Set
[2] View File Contents
[3] Edit File Contents
[4] Clear File Contents
[5] Change File Directory
[6] Quit""")
    
    #A while loop to continue usage for the user until they quit the program
    while True:
        user_select = input("Select from the menu above!: ")
        if user_select.isnumeric() and int(user_select) < 7:
            break
        else:
            continue

    #This option is for creating question sets, utilizing local_count, add_question, add_choices, and add_correct.
    #This option records question count to correctly format the binary code and the specific functions handle input categorization
    #Inputs to the file are also separated by a colon, separating the formatting and the actual user inputs
    if user_select == "1":
        user_input = input("Input the question you want to add: ")
        new_question = Questions(user_input, local_count + 1)
        new_question.write(current_path)
        local_count = ques_count()
        
        for i in range(0, 4):
            user_input = input("Input the choices that you want to add to your question: ")
            new_choice = Choices(user_input, local_count)
            new_choice.write(current_path)

        user_input = input("Input the correct answer from your choices in the question: ")
        new_correct = Corrects(user_input, local_count)
        new_correct.write(current_path)
        print("New question added!")
        continue

    #This option lets the user view the whole contents of the file, also including the line numbers for each line
    #The line numbers in this option's output starts from 0. These line numbers are to be utilized by the user when editing the file
    #This option initializes line_count = 0, opens the file, and uses a for loop to iterate through the lines of the file then prints line number and line itself
    elif user_select == "2":
        line_count = 0
        with open(current_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(f"<line {line_count}>: {line}")
                line_count += 1
        continue
    
    #This option lets the user edit the file contents; asking the user what line number they want to edit and what to replace the line with
    #This option stores the user input into variables and puts them to the parameters of edit_content()
    elif user_select == "3":
        print("Before trying to edit a file, it is advised that the user should view file contents first. "
        "\nThis is to let the user know about the line number to input in editing the file")

        while True:
            user_input = input("Input the line number to edit: ")
            if user_input.isnumeric():
                user_input = int(user_input)
                break
            else: 
                continue
        
        user_edit = input("Input the text to replace current line: ")

        current_path.edit_content(user_input, user_edit)
        print("Done!")

    #This option clears the contents of the file after being given the permission by the user
    #Uses clear_contents() if user answers yes while it breaks the while loop if they answer no
    elif user_select == "4":
        while True:
            user_input = input("This will clear the file's contents. Are you sure? [y/n]: ")
            
            if user_input == "y":
                current_path.clear_contents()
                print("Cleared file contents!")
                break

            elif user_input == "n":
                print("Okay!")
                break
            
            else:
                continue

        continue

    #This option allows the user to change the file that the program will access, storing the file in ../Documents
    #Before proceeding to change the directory, the program first validates the user input. If input is not valid, program asks again.
    #if user_input is none, the program will go back to questions.txt
    elif user_select == "5":
        print("This changes the directory that this program will access. If the file does not exist, it will create it.")

        while True:
            user_input = input("Input the new file to access, no need for \'.txt\' (stored at ../Documents): ")
            valid_flag = True
            for i in user_input:
                if i.isspace():
                    print("Filename cannot contain spaces, try again")
                    valid_flag = False
                    break
                elif i.isalnum() or i in ["-","_"]:
                    valid_flag = True
                    continue
                else: 
                    print("Filename cannot contain symbols other than \'-\' or \'_\'")
                    valid_flag = False
                    break
            
            if valid_flag:
                break
            else:
                continue
        
        if user_input == "":
            user_input = "questions"

        change_path(user_input)

    #This option breaks the whole while loop and ends the program
    elif user_select == "6":
        print("Goodbye!")
        break