import os
class Script:
    def __init__(self, funct, display="No display", descr=""):
        self.funct = funct
        self.display = display
        self.descr = descr
class Gui:
    def __init__(self, title="My script"):
        self.scripts = []
        self.title = title
    def addScript(self, script:Script):
        self.scripts.append(script)
    def setTitle(self, title):
        self.title = title
    def run(self):
        os.system("clear")
        newLineChar = "\n"
        menu = f"{newLineChar}{f'{newLineChar}'.join([f'    [{i + 1}] {display}' for (i, display) in enumerate([x.display for x in self.scripts])])}"
        menu += "\n    [0] Exit"
        print(f"{self.title}" + menu)
        choice = ""
        while choice != "0":
            choice = input("> ")
            if choice.isnumeric() and choice != "0":
                if int(choice) < len(self.scripts):
                    self.scripts[int(choice)-1].funct()
                else:
                    print("Invalid Choice" + menu)
            elif choice == "0":
                break
            else:
                print("Invalid choice" + menu)
        os.system("clear")
