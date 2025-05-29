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

    #to return a specific question
    def get_question(path: str, code: int) -> str:
        break_flag = False

        with open(path, "r") as file:
            content = file.readlines()

            for i in content:
                if i.startswith(f"<{code:b}> <question>"):
                    spec_ques = i
                    break_flag = True

                elif break_flag:
                    break

                else:
                    continue

            return spec_ques.replace(f"<{code:b}> <question>:", "")