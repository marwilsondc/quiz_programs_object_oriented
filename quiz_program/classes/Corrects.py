class Corrects:
    
    def __init__(self, content, code):
        self.content = content
        self.code = code
    
    #to return correct answer objects as strings
    def __str__(self):
        return f"{self.content}"
    
    #to write correct answers in file
    def write(self, path):
        new_line = "\n"

        with open(path, "a") as file:
            file.write(f"<{self.code:b}> <correct>:{self.content}{new_line}")