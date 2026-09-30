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
  
Para poder representar formalmente una Máquina de Turing (MT), habitualmente definimos una séptupla M:

* $Q$: Conjunto finito de estados.
* $\Sigma$: Alfabeto de entrada (sin el símbolo blanco).
* $\Gamma$: Alfabeto de la cinta (contiene a $\Sigma$ y al símbolo blanco).
* $\delta$: Función de transición (las reglas de movimiento).
* $q_0$: Estado inicial.
* $\square$: El símbolo blanco (especificado explícitamente en $\Gamma$).
* $F$: El conjunto de estados de aceptación o parada.

En este caso excluimos el estado final, y lo interpretamos como el estado de parada al que apunta la codificación, y el blanco (□) que representa el límite de la cinta, asumiendo que la cadena de entrada es semánticamente correcta.

Entonces la información a definir en nuestro código para cada MT es la función de transición ($\delta$) . Ya que cada regla va a incluir los datos que nos faltaban, miembros de la quíntupla: (estado_actual, simbolo_leido, nuevo_estado, simbolo_escrito, direccion).

Para que la simulación funcione como una Máquina de Turing Universal (MTU), el programa debe recibir como parámetros de entrada tanto la codificación de estas quíntuplas como la cadena de datos a procesar. 
Para realizar el ejercicio, el código de nuestra MTU cuenta con restricciones de diseño para garantizar que procese el escenario de la MT propuesta en el ejercicio 4, y también otras MT que cumpla obligatoriamente con las siguientes condiciones:

El código procesa únicamente cadenas de entradas binarias (0 y 1) y el símbolo blanco. 
Solo contempla los movimientos izquierda y derecha.
Esto quiere decir que cualquier intento de usar un símbolo distinto (2,3,a,b) requeriría modificar el código fuente, así como no se contempla el movimiento S (Stay), donde el cabezal escribe pero no se mueve.

La MTU se encuentra en el archivo MTU.py


## 6. **Pruebas de funcionamiento**


Probaremos la MT diseñada en el punto 4, que recibe una cadena binaria y retorna todos sus símbolos en 0. Su codificación es: (00,00,00,00,0) (00,01,00,00,0) (00,10,01,10,0)

Cadena de entrada: 110011
<img width="569" height="750" alt="image" src="https://github.com/user-attachments/assets/be274828-7ec7-4b9b-a766-90a7664b6c41" />

Prueba 2: Cadena de entrada 1111
<img width="496" height="561" alt="image" src="https://github.com/user-attachments/assets/c5f42f7c-3ade-4e0c-b0bb-7fbf54df2f63" />


Prueba 3: Cadena de entrada 0000
<img width="530" height="572" alt="image" src="https://github.com/user-attachments/assets/59f89ac1-0bf1-471a-add8-ad18dce31d32" />



## 6. **Informe final**

Explicar la codificación utilizada
		
		La codificación permite representar cualquier regla de transición de una Máquina dE Turing (MT) utilizando un alfabeto estrictamente binario. 
		Cada regla se compone de una quíntupla (Estado_Actual, Símbolo_Leído, Nuevo_Estado, Símbolo_Escrito, Dirección).
		Llegamos a la codificación gracias a la tabla de transiciones 

		<img width="603" height="239" alt="image" src="https://github.com/user-attachments/assets/f17bfc3e-0afb-47c9-931f-e89a506ebb11" />

		Se codifica 1 como representante binario de la izquierda, y 0 como representante de la derecha.

		Esto se entiende como que desde el estado Q0 leyendo 0, su  nuevo estado es q0, escribe 0 y se mueve a la derecha. La codificación es entonces esta misma transición representada por su contraparte binaria 		de la tabla codificada. Siendo la primera transición: 00,00,00,00,0
		
		En el caso de la lectura de un blanco, que indica el final, leemos que desde q0, leyendo blanco, su nuevo estado es qF, escribe blanco y se mueve a la derecha, siendo su codificación:
		00,10,01,10,0.
		
		Las reglas entonces, se traducen brevemente como una serie de pasos:
		Regla 1: Estando en 00, lee 0  pasa a 00, escribe 0, mueve 0. (00,00,00,00,0).
		Regla 2: Estando en 00, lee 1  pasa a 00, escribe 0, mueve 0. (00,01,00,00,0).
		Regla 3: Estando en 00, lee 10  pasa a 01, escribe 10, mueve 0. (00,10,01,10,0).
		
		Es por eso que la codificación de todas sus transiciones es la siguiente:
		
		(00,00,00,00,0) (00,01,00,00,0) (00,10,01,10,0)

		
Mostrar ejemplos de ejecución

		Se utilizó inteligencia artificial para codificar dos nuevas MT que respeten nuestras restricciones de diseño (alfabeto 0 y 1, movimientos solo L y R)
		MT que invierte : Convierte los 0 en 1 y los 1 en 0.

		(00,00,00,01,0) (00,01,00,00,0) (00,10,01,10,0)

		<img width="551" height="751" alt="image" src="https://github.com/user-attachments/assets/9587bd0c-21eb-4887-847c-41050b03ee7c" />


		 MT que recibe una cadena binaria y retorna todos sus símbolos en 1:
		
		(00,00,00,01,0) (00,01,00,01,0) (00,10,01,10,0)

		<img width="512" height="763" alt="image" src="https://github.com/user-attachments/assets/2b98bd20-bbb7-4411-a14a-be9138e552c5" />

		Para finalizar las pruebas, realizamos el comportamiento de esta última MT, pero con una cadena no permitida.

		<img width="499" height="284" alt="image" src="https://github.com/user-attachments/assets/3217610e-4818-435f-a1fa-e16d99154d38" />

Reflexionar sobre la relación entre la MTU y las computadoras modernas
		
		Como reflexión inicial entre la MTU y la computación moderna, es imposible no hacer referencia a la idea de lo que sucede “detrás de escenas”, en donde en nuestra MTU, podemos codificar distintos estados, 		símbolos y movimientos en transiciones representadas de manera binaria, al igual que hoy en día, toda la información se procesa en este mismo sistema numérico y permite, en procesadores de 64 bits, 				representar más de 18 trillones de direcciones únicas de memoria.

		Independientemente de la idea de “múltiples acciones codificadas en binario”, hay una comparación entre hardware y software que Turing representó mucho antes en la cinta codificada. Se trata de la 				distinción entre la máquina física y las reglas del programa, ya que anteriormente para ejecutar distintas reglas se necesitaba una máquina diferente, y con la implementación de la MTU, se demostró que una 		misma máquina física era capaz de comportarse como otras, permitiendo que hoy se entienda a gran escala a la MTU como un procesador, la cinta como memoria RAM, y la codificación de las transiciones, y la MT 		de entrada, como el software a ejecutar.




