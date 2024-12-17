"""
A basic forth-like math interpreter for make basical arithmetic
A program for begginers
"""

lexical = {
    "operators": {
        "add": "+",
        "sub": "-",
        "mul": "*",
        "div": "/",
        # BONUS :
        "sum": "sum",
        "avrg": "avrg",
        "sort": "sort",
        "len": "len",
        "clear": "clr",
        "dup": "dup",
        "switch": "swt",
        "reverse": "rev",
        "iter": "++"
    }
}

class Parser():
    class SyntaxError(BaseException): ...

    def __init__(self) -> None:
        pass

    def isnumber(self, token:str) -> bool:
        try:
            float(token)
            return True
        except: return False

    def isoperator(self, token:str) -> bool:
        return token in lexical["operators"].values()

    def parse(self, to_parse:str) -> list:
        parsed = []

        tokens = to_parse.split()

        for token_index, token in enumerate(tokens):
            if self.isnumber(token):
                parsed.append(["NB", token])
            elif self.isoperator(token):
                parsed.append(["OP", token, list(lexical["operators"].keys())[list(lexical["operators"].values()).index(token.lower())]])
            else:
                raise self.SyntaxError(token, token_index)

        return parsed

class Interpreter():
    class EmptyStack(BaseException): ...

    def __init__(self) -> None:
        self.stack = []

    def int_else_float(self, nb:any) -> any:
        return int(float(nb)) if int(float(nb)) == float(nb) else float(nb)
    
    def interprete(self, parsed:list) -> None:
        for element_index, element in enumerate(parsed):
            element_type = element[0]
            element_token = element[1]
            
            if element_type == "NB":
                self.stack.append(self.int_else_float(element_token))
            elif element_type == "OP":
                element_operator = element[2]
                
                try:
                    if element_operator == "add":
                        b = self.stack.pop()
                        a = self.stack.pop()
                        self.stack.append(a + b)
                    elif element_operator == "sub":
                        b = self.stack.pop()
                        a = self.stack.pop()
                        self.stack.append(a - b)
                    elif element_operator == "mul":
                        b = self.stack.pop()
                        a = self.stack.pop()
                        self.stack.append(a * b)
                    elif element_operator == "div":
                        b = self.stack.pop()
                        a = self.stack.pop()
                        self.stack.append(a / b)
                    # BONUS :
                    elif element_operator == "sum":
                        self.stack.append(sum(self.stack))
                    elif element_operator == "avrg":
                        self.stack.append(sum(self.stack) / len(self.stack))
                    elif element_operator == "sort":
                        self.stack = self.stack.sort()
                    elif element_operator == "len":
                        self.stack.append(len(self.stack))
                    elif element_operator == "clear":
                        self.stack.clear()
                    elif element_operator == "dup":
                        self.stack.append(self.stack[-1])
                    elif element_operator == "switch":
                        self.stack.insert(-1, self.stack.pop())
                    elif element_operator == "iter":
                        self.stack[-1] += 1
                    elif element_operator == "reverse":
                        self.stack.reverse()
                except IndexError:
                    raise self.EmptyStack(element_token, element_index)

if __name__ == "__main__":
    interpreter = Interpreter()
    parser = Parser()

    while running := True:
        to_parse = input(">>> ")
        if to_parse.strip().lower() in ["exit", "quit"]:
            break
        to_interprete = parser.parse(to_parse)
        interpreter.interprete(to_interprete)
        print("Stack :", interpreter.stack)
