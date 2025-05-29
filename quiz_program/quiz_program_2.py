#import Questions
from classes.Questions import Questions

#import Choices
from classes.Choices import Choices

#import Corrects
from classes.Corrects import Corrects

#import FilePath
from classes.FilePath import FilePath 

#import time
import time

#import random
import random

current_path = FilePath("questions.txt")

#define change_path for changing file being accessed
def change_path(new_file: str):
    global current_path
    current_path = FilePath(new_file)

#define ques_count() to return number of questions
def ques_count():
    with open(current_path, "r") as file:
        content = file.read()
        return content.count("<question>")
    
#define check_ans()
def check_ans(user_input: str, correct: str) -> bool: 
    if user_input == correct:
        return True
    
    else:
        return False

#check if current_path exists, set file_exists to True if so, otherwise False
if current_path.path.exists():
    file_exists = True

else:
    print("Error: questions.txt does not exist")
    time.sleep(1)
    print("Create a question file first, then run this program")
    file_exists = False

#initiate conditional infinite while loop
while file_exists:

    #initialize ques_dict
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
                    ques_dict[insert_code] = Questions(unclean_code[1], clean_code[0])

    #initialize local_count and local_path_var and ques_range
    local_ques_count = ques_count()
    local_path_var = current_path
    ques_range = range(1, local_ques_count + 1)

    #Create the main menu:
    print(f"""
Welcome to the Quizzler!

File currently opened: {local_path_var}
There are {local_ques_count} questions in this file.
Main Menu:

[1] Ask Random Question
[2] Ask All Questions
[3] Change Directory
[4] Quit Program
""")
    #Create prompt to choose among the given options
    while True:
        user_select = input("Select from the menu above!: ")
        if user_select.isnumeric() and int(user_select) < 5:
            break
        else:
            continue
    
    user_select = int(user_select)

    #option: Ask random question; program asks a random question
    if user_select == 1:
        rand_ques_code = random.choice(ques_range)
        print("Okay! Giving you a random question now: ")
        print(Questions.get_question(local_path_var, rand_ques_code))

        for i in Choices.get_choices(local_path_var, rand_ques_code):
            print(i)

        correct_ans = Corrects.get_correct(local_path_var, rand_ques_code)

        time.sleep(3)
        user_ans = input("Choose your answer: ")

        if check_ans(user_ans, correct_ans):
            print("Very good! You answered correctly!")
            time.sleep(1)

        else:
            print(f"Sorry, your answer is wrong! The answer was: {correct_ans}")
            time.sleep(1)

    #option: Ask all questions; still random, but asks all questions
    elif user_select == 2:
        print("The program will now ask you all the questions in this file")
        time.sleep(1)
        print("There will be no particular flow in the asking of questions, all questions will be given at random.")
        time.sleep(1)
        print("Once all questions are asked, the session will end")
        time.sleep(1)
        print("Session begins now...")

        asked_codes = list()
        questions_asked = len(asked_codes)
        score = 0

        while questions_asked != local_ques_count:
            break_flag = False
            rand_ques_code = random.choice(ques_range)
            
            if rand_ques_code in asked_codes:
                continue

            else:
                print(Questions.get_question(local_path_var, rand_ques_code))
                for i in Choices.get_choices(local_path_var, rand_ques_code):
                    print(i)

                correct_ans = Corrects.get_correct(local_path_var, rand_ques_code)
                asked_codes.append(rand_ques_code)
                questions_asked += 1

                time.sleep(3)
                user_ans = input("Input your answer: ")

                if check_ans(user_ans, correct_ans):
                    time.sleep(1)
                    print("Very good! Onto the next question!")
                    score += 1


                else:
                    print(f"Your answer is wrong! The answer was {correct_ans}")
                    time.sleep(2)

                    while True: 
                        user_select = input("Continue session? (y/n): ")
                        if user_select.isalpha() and user_select == "y":
                            break

                        elif user_select.isalpha() and user_select == "n":
                            break_flag = True
                            print("Ending session...")
                            time.sleep(1)
                            break

                        else: 
                            continue
                
                if break_flag:
                    break
        
        print(f"You answered {score} questions right!")


    #option: Change directory; change which file the program will access
    elif user_select == 3:
        print("If you want to change the file to access, it is recommended that you first create a text file with the quiz creator.")
        time.sleep(1)
        print("Input the name of the file you want to access (without the file extension or \".txt\")")
        time.sleep(1)
        file_change = input("File name: ")
        
        current_path = FilePath(file_change)
        print(f"Done! Moved to {current_path}")

    #option: Quit program; breaks the loop and closes the program
    elif user_select == 4:
        break