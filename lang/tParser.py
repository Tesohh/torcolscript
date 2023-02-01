from logs import log
# import sympy
import ast
import operator as op

torcolMem = {
    "fassavalley": "bestiale",
}
# operatori validi
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

# una sorta di eval ma sicuro che non permette di mettere funzioni
def calculateExpression(expression: str):
    return evalSpecial(ast.parse(expression, mode='eval').body)

def evalSpecial(element):
    if isinstance(element, ast.Num): # <number>
        return element.n
    elif isinstance(element, ast.BinOp): # <left> <operator> <right>
        return operators[type(element.op)](evalSpecial(element.left), evalSpecial(element.right))
    elif isinstance(element, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(element.op)](evalSpecial(element.operand))
    else:
        raise TypeError(element)

# prendi dal dizionario torcolMem una variabile
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
        elif w.startswith("="):
            w = w.replace("=", "")
            try:
                w = str(calculateExpression(w))
            except:
                log(f"errore nel calcolo {w}", 2)
                exit()
        elif w.startswith("!!"):
            w = w.replace("!!", "")
            w = eval(w)
        words[i] = w
    return words


def execTorcol(words: list[str]):
    command = words[0]
    words = replacer(words)
    if command == 'stampa':
        for i in words[1:]:
            print(i, end=" ")
        print("")

    elif command == "metiitezeche" | "meti":

        getVarFromMem(words[1])
        metimento = input(' '.join(words[2:])).strip()
        try:
            metimento = float(metimento)
        except:
            pass
        torcolMem[words[1]] = metimento

    elif command == 'defenir' | 'def':
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

    elif command == "fadoiconc":
        operator = words[3]
        getVarFromMem(words[1])  # da errore se non esiste la variabile

        try:
                if operator == "+":
                    torcolMem[words[1]] = float(words[2]) + float(words[4])
                elif operator == "-":
                    torcolMem[words[1]] = float(words[2]) - float(words[4])
                elif operator == "*":
                    torcolMem[words[1]] = float(words[2]) * float(words[4])
                elif operator == "/":
                    torcolMem[words[1]] = float(words[2]) / float(words[4])

                elif operator == "==":
                    torcolMem[words[1]] = words[2] == words[4]
                elif operator == ">":
                    torcolMem[words[1]] = float(words[2]) > float(words[4])
                elif operator == ">=":
                    torcolMem[words[1]] = float(words[2]) >= float(words[4])
                elif operator == "<":
                    torcolMem[words[1]] = float(words[2]) < float(words[4])
                elif operator == "<=":
                    torcolMem[words[1]] = float(words[2]) <= float(words[4])
                else:
                    log(f"Operator {operator} no troado", 2)
                    exit()
        except ValueError:
            log("tas metù ite na corda", 2)
            exit()

    elif command == "se":
        if words[1] == True:
            execTorcol(words[2:])
    elif command == "ripeter":
        if len(words) > 2:
            for i in range(int(words[1])): execTorcol(words[2:])

    else:
        if command != "":
            log(f"Ordinanza {command} no troada", 2)
            exit()

    


def torcler(script: str):
    lines = script.splitlines()
    for i in lines:
        words = i.split(" ")
        execTorcol(words)
