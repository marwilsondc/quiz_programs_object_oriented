import pathlib

class FilePath(pathlib):

    #filepath initialization and make file on initialization, do nothing if file exists
    def __init__(self, filename):
        self.filename = filename
        self.path = pathlib.Path("~", "Documents", self.filename).expanduser()
        self.path.parent.mkdir(exist_ok = True, parents = True)

    #return filename when called
    def __str__(self):
        return f"{self.filename}"

    #return current directory
    def current_dir(self) -> str:
        with open(self.path, "r") as file:
            return pathlib.Path(file.name)
        
    #edit file contents 
    #clears file contents and rewrites it with the edited line
    def edit_content(self, line_num: int, text: str): 
        new_line = "\n"

        with open(self.path, "r") as file:
            lines = file.readlines()
    
        try:
            bin_code = lines[line_num].split(":")
            bin_code = bin_code[0]

        except IndexError or UnboundLocalError:
            pass

        if line_num <= len(lines):
            if "<question>" in bin_code:
                lines[line_num] = f"{bin_code}:{text}{new_line}"
            
            elif "<choice>" in bin_code or "<correct>" in bin_code:
                lines[line_num] = f"{bin_code}:{text}{new_line}"

            with open(self.path, "w") as file:
                for line in lines:
                    file.write(line)
        
        else: 
            print("Line", line_num, "not in file.")
            print("File has", len(lines), "lines.")