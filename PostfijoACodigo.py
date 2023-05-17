"""
a=a1+
t1=a
t2=1
t3=t1+t2
a=t3
"""
class PostfijoACodigo:

    def __init__(self):
        self.stack = []
        self.operadores = ['+', '-', '*', '/', '^']
        self.code = ""
        self.numberOfTerms = 1
  
    def PostfijoACodigo(self, line):
    
        final = ""
        equalFlag = 0
        for token in line:
            if token in self.operadores:
                if len(self.stack) >= 2:
                    operator1 = self.stack.pop()
                    operator2 = self.stack.pop()
                    
                    self.code += f"t{self.numberOfTerms}={operator2}{token}{operator1}\n"
                    self.stack.append(f"t{self.numberOfTerms}")
                    self.numberOfTerms += 1 
                else:
                    return "Bad syntax."
            elif equalFlag:
                self.stack.append(token)
            elif token == '=':
                final += token
                equalFlag = 1
            else:
                final += token
            

        if len(self.stack) > 1:
            return "Bad syntax"
        elif len(self.stack) == 1:
            final += self.stack.pop()
        
        self.code += final
        
        return self.code


pac = PostfijoACodigo()
print(pac.PostfijoACodigo("b=cae+-"))

