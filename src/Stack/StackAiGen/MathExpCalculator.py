from src.Stack.StackAiGen.Stack import Stack


class MathExpCalculator:
    PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}

    def __init__(self):
        self.stack = Stack()
        # "-" can't be the delimiter because it's also the minus operator
        self.delimiter = " "

    def run(self, expression):
        wff = self.get_wff(expression)
        postfix = self.to_postfix(wff)
        return self.calculate(postfix)

    # wff = well formed formula: every token separated by the delimiter
    # e.g. "12+(3*-4)" -> "12 + ( 3 * -4 )"
    def get_wff(self, expression):
        expression = expression.replace(" ", "")
        wff = ""
        prev = None  # type of the previous token: None, "num", "op", "(", ")"
        i = 0
        n = len(expression)

        while i < n:
            ch = expression[i]
            unary_minus_number = (
                    ch == "-" and prev in (None, "(", "op")
                    and i + 1 < n and (expression[i + 1].isdigit() or expression[i + 1] == ".")
            )

            if ch.isdigit() or ch == "." or unary_minus_number:
                # read the whole number (multi-digit, decimals, leading minus)
                start = i
                i += 1
                while i < n and (expression[i].isdigit() or expression[i] == "."):
                    i += 1
                wff += expression[start:i] + self.delimiter
                prev = "num"
                continue

            if ch == "-" and prev in (None, "("):
                # unary minus before a parenthesis: -(2+3) -> 0 - (2+3)
                wff += "0" + self.delimiter + "-" + self.delimiter
                prev = "op"
            elif self.is_operator(ch):
                if prev in (None, "(", "op"):
                    raise ValueError(f"Operator '{ch}' is in the wrong place")
                wff += ch + self.delimiter
                prev = "op"
            elif ch == "(":
                wff += ch + self.delimiter
                prev = "("
            elif ch == ")":
                wff += ch + self.delimiter
                prev = ")"
            else:
                raise ValueError(f"Invalid character: '{ch}'")
            i += 1

        return wff.strip()

    # infix -> postfix (shunting-yard algorithm) using our Stack
    def to_postfix(self, wff):
        operators = Stack()
        postfix = ""

        for token in self.tokenize(wff):
            if self.is_number(token):
                postfix += token + self.delimiter
            elif token == "(":
                operators.push(token)
            elif token == ")":
                while not operators.is_empty() and operators.peek() != "(":
                    postfix += operators.pop() + self.delimiter
                if operators.is_empty():
                    raise ValueError("Mismatched parentheses")
                operators.pop()  # throw away the "("
            else:  # operator
                while (not operators.is_empty()
                       and operators.peek() != "("
                       and self.PRECEDENCE[operators.peek()] >= self.PRECEDENCE[token]):
                    postfix += operators.pop() + self.delimiter
                operators.push(token)

        while not operators.is_empty():
            op = operators.pop()
            if op == "(":
                raise ValueError("Mismatched parentheses")
            postfix += op + self.delimiter

        return postfix.strip()

    def tokenize(self, wff):
        return wff.split(self.delimiter)

    def calculate(self, postfix):
        self.stack.clear()

        for token in self.tokenize(postfix):
            if self.is_operator(token):
                if self.stack.size() < 2:
                    raise ValueError("Malformed expression")
                right = self.stack.pop()  # popped first = right-hand side
                left = self.stack.pop()
                self.stack.push(self.apply_operator(left, right, token))
            else:
                self.stack.push(float(token))

        if self.stack.size() != 1:
            raise ValueError("Malformed expression")

        result = self.stack.pop()
        return int(result) if result.is_integer() else result

    def apply_operator(self, left, right, op):
        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if op == "/":
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        raise ValueError(f"Unknown operator: {op}")

    def is_operator(self, token):
        return token in ("+", "-", "*", "/")

    def is_number(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False
