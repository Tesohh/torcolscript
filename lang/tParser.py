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
        elif w.startswith("!!"):
            w = w.replace("!!", "")
            w = eval(w)
        words[i] = w
    return words


def execTorcol(words: list[str]):
    command = words[0]
    words = replacer(words)

    match command:
        case 'stampa':
            for i in words[1:]:
                print(i, end=" ")
            print("")

        case "metiitezeche" | "meti":

            getVarFromMem(words[1])
            metimento = input(' '.join(words[2:])).strip()
            try:
                metimento = float(metimento)
            except:
                pass
            torcolMem[words[1]] = metimento

        case 'defenir' | 'def':
            key = words[1].replace("$", "")
            if len(words) >= 2:
                value = ' '.join(words[2:])
            else:
                value = 0

            try:
                value = int(value)
            except:
                pass

            if value == "vera":
                value = True
            elif value == "faus":
                value = False

            torcolMem[key] = value

        case "fadoiconc":
            operator = words[3]
            getVarFromMem(words[1])  # da errore se non esiste la variabile

            try:
                match operator:
                    case "+":
                        torcolMem[words[1]] = float(words[2]) + float(words[4])
                    case "-":
                        torcolMem[words[1]] = float(words[2]) - float(words[4])
                    case "*":
                        torcolMem[words[1]] = float(words[2]) * float(words[4])
                    case "/":
                        torcolMem[words[1]] = float(words[2]) / float(words[4])

                    case "=":
                        torcolMem[words[1]] = words[2] == words[4]
                    case ">":
                        torcolMem[words[1]] = float(words[2]) > float(words[4])
                    case ">=":
                        torcolMem[words[1]] = float(words[2]) >= float(words[4])
                    case "<":
                        torcolMem[words[1]] = float(words[2]) < float(words[4])
                    case "<=":
                        torcolMem[words[1]] = float(words[2]) <= float(words[4])
                    case _:
                        log(f"Operator {operator} no troado", 2)
                        exit()
            except ValueError:
                log("tas metù ite na corda coion", 2)
                exit()

        case "se":
            if words[1] == True:
                execTorcol(words[2:])
        case "ripeter":
            if len(words) > 2:
                for i in range(int(words[1])): execTorcol(words[2:])

        case _:
            if command != "":
                log(f"Ordinanza {command} no troada", 2)
                exit()

    


def torcler(script: str):
    lines = script.splitlines()
    for i in lines:
        words = i.split(" ")
        execTorcol(words)
