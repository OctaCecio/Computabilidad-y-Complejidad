## 1. **¿Por qué se dice que una MTU es capaz de simular cualquier Máquina de Turing?**

Una MTU puede simular cualquier máquina de Turing, ya que actúa como intérprete universal, su funcionamiento se basa en recibir la codificación de una máquina de Turing, y una cadena de entrada, la cual procesa comportándose como lo haría la MT de entrada.

## 2. **Suponer que se tiene una MT M que acepta todas las cadenas que terminan en 01. Indicar qué debería hacer una MTU con las siguientes entradas. Explicar en cada caso si la MTU acepta o rechaza y por qué** 

Las siguientes entradas representan la máquina de turing de entrada (M) y las cadenas a analizar, cómo sabemos que la MT M acepta todas las cadenas que terminan en 01, podemos determinar que: 
U(⟨M⟩,1101) = MTU acepta la cadena.
U(⟨M⟩,100) = MTU rechaza la cadena.
U(⟨M⟩,01) = MTU acepta la cadena.
U(⟨M⟩,111) = MTU rechaza la cadena.

## 3. **Dada la siguiente MT M:**
<img width="240" height="157" alt="image" src="https://github.com/user-attachments/assets/17f281d2-cf28-4d2a-b965-9df474d356d9" />
  1. Explicar que hace M

    M es una MT que procesa una cadena de dos símbolos en binario, modificando el primero por su opuesto.


  2.  Explicar qué información debería recibir una MTU para poder simular M

    La MTU debe recibir la codificación de M, y la cadena a analizar.

  3.  Codificar la cintar de MTU sabiendo que configuración de la cinta de MT M es 1 q0 0 1 1

    Para la  codificación realizamos la tabla codificada de transiciones:

  <img width="554" height="154" alt="image" src="https://github.com/user-attachments/assets/cc557623-13d8-43c4-a5e2-1454e1d76fed" />

  1*11$000#0000110#0010100#0101000#0111010

¿Como se hace? El ejercicio nos da la configuración inicial de la MT M:
	1 q0 0 1 1
Esto quiere decir que la cinta de la máquina ya procesó un 1, actualmente está en q0, leyendo el símbolo inmediato a su derecha, 0, y le falta por leer 11.
El estado actual se debe sacar de la secuencia, nos sirve para entender en donde se encuentra la cabeza lectora escritora, y el 0, es el símbolo actual, por lo que lo reemplazamos por * que representa el cabezal, y lo colocamos inmediatamente a la derecha de la cadena después de $, que representa el estado actual y el símbolo leído.

## 4. **Codificación de una máquina simple**

  Definir una máquina M y codificar sus estados, símbolos y transiciones.
	
	La MT M convierte toda su cinta en símbolos 0.

  <img width="648" height="267" alt="image" src="https://github.com/user-attachments/assets/df62317a-2480-4d2c-a90a-bc617c6b163a" />


Codificaciones: 
(00,00,00,00,0)
(00,01,00,00,0)
(00,10,01,10,0)

## 5. **Simulación básica**
  


