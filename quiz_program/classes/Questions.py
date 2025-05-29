class Questions:

    def __init__(self, content, code):
        self.content = content
        self.code = code 
    
    #return question as string
    def __str__(self):
        return f"The question is {self.content} ({self.code})"

    #to write questions in file
    def write(self, path):
        new_line = "\n"

        with open(path, "a") as file:
            file.write(f"{new_line}<{self.code:b}> <question>:{self.content}{new_line}")
