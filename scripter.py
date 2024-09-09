import sys
import os

# python3 scripter.py x.py
def parseFunc(filestr):
    funcs = []
    imports = []
    pos = 0
    while pos < len(filestr):
        if filestr[pos] == 'def':
            pos += 1
            if filestr[pos][-3:len(filestr[pos])] == '():':
                funcName = filestr[pos][:-3]
                funcs.append(funcName)
            else: 
                continue
        if filestr[pos] == 'import':
            pos += 1
            imports.append(filestr[pos])
        pos += 1
    return (funcs, imports)

def readF(file):
    f = open(file)
    text = f.read()
    f.close()
    return text

def buildRunScript(name):
    imported = sys.argv[1][:-3]
    endres = f"from gui import Gui, Script\nimport {imported}\ng = Gui('{name}')\n"
    with open(sys.argv[1]) as file:
        f = file.read()
        f = f.split()
        (funcs, imports) = parseFunc(f)
        endres += f"{'\n'.join(['import ' + x for x in imports])}\n"
        for func in funcs:
            endres += f"g.addScript(Script({imported}.{func}, ' '.join([x for x in {imported}.{func}.__doc__.split(' ') if x != '']).replace('\\n','\\n       ')))\n"
        endres += f"g.run()"
        with open("scripterRun.py", 'w+') as r:
            r.write(endres)
        import scripterRun
        os.remove("scripterRun.py")

def buildFullScript(name):
    gui = readF("gui.py")
    f = readF(sys.argv[1])
    endres = f"{f}\n{gui}\ng = Gui('{name}')\n"
    f = f.split()
    funcs = parseFunc(f)
    for func in funcs[0]:
        endres += f"g.addScript(Script({func}, ' '.join([x for x in {func}.__doc__.split(' ') if x != '']).replace('\\n','\\n       ')))\n"
    endres += f"g.run()"
    with open("scripterRun.py", 'w+') as r:
        r.write(endres)

if __name__ == "__main__":
    title = "My script"
    if len(sys.argv) > 2 and sys.argv[2] == "-s":
        title = input("Script name: ")
        buildFullScript(title)
    else:
        buildRunScript(title)
