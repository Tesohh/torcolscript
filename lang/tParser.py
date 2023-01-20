from logs import log
import sympy

torcolMem = {
    "fassavalley": "bestiale",
    "numer": 3
}


def getVarFromMem(key: str):
    key = key.replace("$", "")
    try:
        return torcolMem[key]
    except KeyError:
        log(f"Variabile `{key}` no troada", 2)
        exit()


def replacer(words: list[str]):
    for i in range(len(words)):
        w = words[i]
        if w.startswith("$"):
            w = getVarFromMem(w)
        elif w.startswith("=="):
            w = w.replace("==", "")
            w = float(sympy.sympify(w))
        words[i] = w
    return words


def execTorcol(words: list[str]):
    command = words[0]
    words = replacer(words)

    if command == 'stampa':
        for i in words[1:]:
            print(i, end=" ")
        print("")

    elif command == 'defenir' or command == 'def':
        key = words[1].replace("$", "")
        value = words[2]

        # if value.startswith("$"):
        #     value = getVarFromMem(value)
        # elif value.startswith("=="):
        #     value = value.replace("==", "")
        #     value = eval(value)

        try:
            value = int(value)
        except:
            pass

        if value == "vera":
            value = True
        elif value == "faus":
            value = False

        torcolMem[key] = value

    elif command == "fadoiconc":
        operator = words[3]
        getVarFromMem(words[1])  # da errore se non esiste la variabile

        if operator == "+":
            torcolMem[words[1]] = float(words[2]) + float(words[4])
        elif operator == "-":
            torcolMem[words[1]] = float(words[2]) - float(words[4])
        elif operator == "*":
            torcolMem[words[1]] = float(words[2]) * float(words[4])
        elif operator == "/":
            torcolMem[words[1]] = float(words[2]) / float(words[4])

    elif command == "meti_ite_zeche" or command == "meti":
        getVarFromMem(words[1])


def torcler(script: str):
    lines = script.splitlines()
    for i in lines:
        words = i.split(" ")
        execTorcol(words)
