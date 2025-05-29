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

    #to return specific choices in lists
    def get_choices(path: str, code: int) -> list:
        choice_list = list()
        break_flag = False

        with open(path, "r") as file:
            content = file.readlines()
            
            for i in content: 
                if i.startswith(f"<{code:b}> <choice>"):
                    choice_list.append(i.replace(f"<{code:b}> <choice>:", ""))
                    break_flag = True
                
                elif break_flag:
                    break

                else:
                    continue
            
            return choice_list