class TraductorInfijoPosfijo:
    def __init__(self):
        self.pila = []
        self.precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def traducir(self, expresion_infija):
        expresion_posfija = []
        tokens = expresion_infija.split()

        for token in tokens:
            if self.es_numero(token) or self.es_variable(token):
                expresion_posfija.append(token)
            elif self.es_operador(token):
                while (self.pila and self.precedencia.get(token, 0) <= self.precedencia.get(self.pila[-1], 0)):
                    expresion_posfija.append(self.pila.pop())
                self.pila.append(token)
            elif token == '(':
                self.pila.append(token)
            elif token == ')':
                while self.pila and self.pila[-1] != '(':
                    expresion_posfija.append(self.pila.pop())
                self.pila.pop()

        while self.pila:
            expresion_posfija.append(self.pila.pop())

        return ' '.join(expresion_posfija)

    def es_numero(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def es_variable(self, token):
        return token.isalpha()

    def es_operador(self, token):
        return token in ['+', '-', '*', '/', '^']


# Ejemplo de uso
expresion_infija = '5 + 4 * 3 - 2 / 1'
traductor = TraductorInfijoPosfijo()
expresion_posfija = traductor.traducir(expresion_infija)
print(expresion_posfija)
