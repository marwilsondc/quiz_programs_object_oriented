class Choices: 
    
    def __init__(self, content, code):
        self.content = content
        self.code = code

    #to return choice as string
    def __str__(self):
        return f"{self.content}"
    
    #to write choice in file
    def write(self, path):
        new_line = "\n"

        with open(path, "a") as file:
            file.write(f"<{self.code:b}> <choice>:{self.content}{new_line}")