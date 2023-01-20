class col:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pprint(script: str):
    cat = ""
    lines = script.splitlines()
    for l in lines:
        words = l.split(" ")
        print(col.RED, end=" ")
        for w in words:
            if w.startswith("$"):
                w = f"{col.GREEN}{w}"
            elif w.startswith("=="):
                w = f"{col.CYAN}{w}"
            print(w, end=f"{col.ENDC} ")
        print("")
