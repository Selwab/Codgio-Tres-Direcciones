class GeneradorCodigoIntermedio:
    def __init__(self):
        self.codigo_intermedio = []
        self.contador_etiquetas = 1

    def generar_etiqueta(self):
        etiqueta = f"L{self.contador_etiquetas}"
        self.contador_etiquetas += 1
        return etiqueta

    def generar_ciclo_while(self, condicion, instrucciones):
        etiqueta_inicio = self.generar_etiqueta()
        etiqueta_fin = self.generar_etiqueta()

        # Agregar instrucciones iniciales antes del ciclo
        self.codigo_intermedio.append(f"{etiqueta_inicio}:")
        self.codigo_intermedio.extend(instrucciones)

        # Generar código para la condición
        self.codigo_intermedio.append(f"{condicion}")
        self.codigo_intermedio.append(f"if t{self.contador_etiquetas-1} goto {etiqueta_fin} else goto {etiqueta_inicio}")

        # Agregar etiqueta de fin del ciclo
        self.codigo_intermedio.append(f"{etiqueta_fin}:")

    def obtener_codigo_intermedio(self):
        return "\n".join(self.codigo_intermedio)


# Ejemplo de uso
generador = GeneradorCodigoIntermedio()

condicion = "t1 = a\n" \
            "t2 = b\n" \
            "t3 = t1 < t2"

instrucciones = ["L2: t4 = a",
                 "t5 = 1",
                 "t6 = t4 + t5",
                 "a = t6",
                 "goto L1"]

generador.generar_ciclo_while(condicion, instrucciones)

codigo_intermedio = generador.obtener_codigo_intermedio()
print(codigo_intermedio)


"""Ahora usadno lo anterior, yo quiero hacer un lenguaje intermedio que me devuelva un ciclo while en esta notación "L1: t1 = a
t2 = b
t3 = t1 < t2
if t3 goto L2 else goto
L3
L2: t4 = a
t5 = 1
t6 = t4 + t5
a = t6
goto L1
L3:
"""