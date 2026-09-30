import time
import re

class MaquinaUniversal:
    def __init__(self, cadena_inicial, transiciones, estado_inicial, estados_aceptacion, simbolo_blanco='_'):
        self.cinta = list(cadena_inicial) if cadena_inicial else [simbolo_blanco]
        self.cabezal = 0
        self.estado = estado_inicial
        self.transiciones = transiciones
        self.estados_aceptacion = estados_aceptacion
        self.simbolo_blanco = simbolo_blanco

    def mostrar_paso(self):
        cinta_str = "".join(self.cinta)
        indicador = " " * self.cabezal + "^"
        print(f"Estado: {self.estado}")
        print(cinta_str)
        print(indicador)
        print("-" * 30)

    def paso(self):
        
        if self.estado in self.estados_aceptacion:
            return False 

        # Expandir cinta si es necesario
        if self.cabezal < 0:
            self.cinta.insert(0, self.simbolo_blanco)
            self.cabezal = 0
        elif self.cabezal >= len(self.cinta):
            self.cinta.append(self.simbolo_blanco)

        simbolo_leido = self.cinta[self.cabezal]
        accion = self.transiciones.get((self.estado, simbolo_leido))

        if accion is None:
            self.estado = 'RECHAZADO_SIN_REGLA'
            return False 

        nuevo_estado, simbolo_escribir, direccion = accion
        self.cinta[self.cabezal] = simbolo_escribir
        self.estado = nuevo_estado

        if direccion == 'R': self.cabezal += 1
        elif direccion == 'L': self.cabezal -= 1
        
        return True

    def ejecutar(self, retardo=0.5):
        print("\n--- INICIANDO EJECUCIÓN ---")
        self.mostrar_paso()
        while self.paso():
            time.sleep(retardo)
            self.mostrar_paso()

        if self.estado in self.estados_aceptacion:
            print("Cadena aceptada y transformada.")
        else:
            print("No hay regla para el estado actual.")

# DECODIFICADOR MTU
def decodificar_reglas(codigo_bruto):
    """
    Busca patrones de 5 números binarios (ej: 00,00,00,00,0)
    y los traduce al formato interno de la máquina.
    """
    # Ignorar parentesis y espacios para obtener la expresión regular de la quintupla de la MT.
    patron = r'([01]+)\s*,\s*([01]+)\s*,\s*([01]+)\s*,\s*([01]+)\s*,\s*([01]+)'
    tuplas_encontradas = re.findall(patron, codigo_bruto)
    
    transiciones = {}
    
    map_simbolos = {'00': '0', '01': '1', '10': '_'}
    map_direcciones = {'0': 'R', '1': 'L'}
    
    for t in tuplas_encontradas:
        estado_act = f"q_{t[0]}" 
        simbolo_lei = map_simbolos.get(t[1], t[1])
        estado_nue = f"q_{t[2]}" 
        simbolo_esc = map_simbolos.get(t[3], t[3])
        direccion = map_direcciones.get(t[4], t[4])
        
        transiciones[(estado_act, simbolo_lei)] = (estado_nue, simbolo_esc, direccion)
        
    return transiciones

if __name__ == "__main__":
    print("========================================")
    print("   SIMULADOR DE MÁQUINA DE TURING (MTU) ")
    print("========================================\n")
    
    print("Ingresa las reglas codificadas de la MT.")
    codigo_input = input(">> Código de la MT: ")
    
    print("\nIngresa la cadena de entrada compuesta por 0s y 1s.")
    print("Ejemplo: 10110")
    cadena_input = input(">> Cadena de entrada: ")
    
    reglas_generadas = decodificar_reglas(codigo_input)
    
    if not reglas_generadas:
        print("\n[ERROR] No se detectaron reglas válidas. Revisa la codificación ingresada.")
    else:
        
        mtu = MaquinaUniversal(
            cadena_inicial=cadena_input,
            transiciones=reglas_generadas,
            estado_inicial="q_00",
            estados_aceptacion={"q_01"}
        )
        mtu.ejecutar(retardo=0.8)