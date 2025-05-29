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

    #to return specific correct answers
    def get_correct(path: str, code: int) -> str:
        break_flag = False

        with open(path, "r") as file:
            content = file.readlines()

            for i in content:
                if i.startswith(f"<{code:b}> <correct>"):
                    correct_ans = i.replace(f"<{code:b}> <correct>:", "").replace("\n", "")
                    break_flag = False
                
                elif break_flag:
                    break

                else:
                    continue
            
            return correct_ans