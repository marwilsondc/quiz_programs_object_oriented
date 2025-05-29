#import Questions
from classes.Questions import Questions

#import Choices
from classes.Choices import Choices

#import Corrects
from classes.Corrects import Corrects

#import FilePath
from classes.FilePath import FilePath 

current_path = FilePath("questions.txt")

#define change_path for changing file being accessed
def change_path(new_file: str):
    global current_path
    current_path = FilePath(new_file)

