import tokenize


class MathExpCalculator:
    def __init__(self):
        self.stack = Stack()
        self.delimiter = "-"

    def get_wff(self,expression):
        pass

    def to_postfix(self):
        pass

    def run(self,expression):
        wff = self.get_wtff(expression)
        postfix = self.to_postfix()
        result = self.calculate(postfix)
        return result
#wff means well formed formula we basically convert so that it its proper
    def tokenize(self,wff):
        return wff.split(self.delimiter)

    def calculate(self,pwff):
        inputs = self.tokenize(pwff)
        counter = 0
        self.stack.push(inputs[0])
        while not self.stack.isEmpty() and counter = inputs.length():
            counter += 1
            token = inputs[counter]
            if not self.isOperator(token):
                self.stack.push(token)
            first = self.stack.pull()
            second = self.stack.pull()
            result = self.calculate(first,second,token)
            self.stack(result)
        return self.stack.pop()

    def isOperator(self,token):
        if token in ["+","-","*","/"]:
            return True
        return False
