# Problema de Correspondencia de Post (PCP)

## Historia

El **Problema de Correspondencia de Post** fue presentado en **1946** por **Emil Leon Post**, matemático y lógico estadounidense, en el marco de sus investigaciones sobre los límites de la computabilidad.

Su objetivo era estudiar qué problemas podrían resolverse mediante procedimientos mecánicos y cuáles no. A través de un problema aparentemente simple basado en la concatenación de cadenas de símbolos, demostró su **indecidibilidad** —es decir, la inexistencia de un algoritmo general capaz de determinar con certeza y en un tiempo finito si existe o no solución para cualquier caso—.

Posteriormente, el PCP se convirtió en una herramienta fundamental para demostrar la indecidibilidad de otros problemas en la teoría de la computación.

---

## ¿Qué es el Problema de Correspondencia de Post?

El **Problema de Correspondencia de Post (PCP)** es un problema de decisión de la teoría de la computación que consiste en determinar si es posible formar dos cadenas idénticas a partir de dos listas finitas de cadenas de símbolos.

Dadas dos listas $A$ y $B$, cada elemento de $A$ está asociado con uno de $B$ mediante un mismo índice.

El objetivo es encontrar una secuencia finita y no vacía de índices que, al concatenar las cadenas seleccionadas de ambas listas en el mismo orden, produzca exactamente el mismo resultado.

### Condiciones a respetar:
* Los índices pueden elegirse en cualquier orden.
* Un mismo índice puede utilizarse más de una vez.
* Cada índice seleccionado debe ser el mismo para ambas listas.

El problema consiste en determinar si existe o no una secuencia que cumpla esta igualdad.

---

## Ejemplo 1: Representación del PCP mediante fichas de dominó

Una forma visual de comprender el PCP es mediante fichas de dominó, donde cada ficha representa un par de cadenas: una en la parte superior y otra en la inferior.

### Conjunto de Fichas:

| Ficha 1 | Ficha 2 | Ficha 3 | Ficha 4 |
| :---: | :---: | :---: | :---: |
| $\frac{\text{b}}{\text{ca}}$ | $\frac{\text{a}}{\text{ab}}$ | $\frac{\text{ca}}{\text{a}}$ | $\frac{\text{abc}}{\text{c}}$ |

### Resolución paso a paso:
1. Para comenzar, elegimos la **Ficha 2** ($\frac{\text{a}}{\text{ab}}$), ya que ambas cadenas empiezan con el mismo símbolo (`a`).
2. A partir de ahí, seleccionamos las siguientes fichas buscando compensar los símbolos que van quedando pendientes en alguna de las dos cadenas.
3. Siguiendo este procedimiento, obtenemos la secuencia de fichas: **$2 \rightarrow 1 \rightarrow 3 \rightarrow 2 \rightarrow 4$**.

#### Concatenación resultantes:
* **Cadena superior:** $\text{a} + \text{b} + \text{ca} + \text{a} + \text{abc} = \mathbf{ABACAAABC}$
* **Cadena inferior:** $\text{ab} + \text{ca} + \text{a} + \text{ab} + \text{c} = \mathbf{ABACAAABC}$

Como ambas cadenas son iguales, encontramos una solución para esta instancia del PCP.

---

## Ejemplo 2: Representación del PCP mediante tabla

El PCP también puede representarse mediante una tabla, donde dadas dos listas $A$ y $B$ de cadenas sobre un alfabeto, hay que determinar si existe una concatenación de la forma:

$$x_{i_1} x_{i_2} \dots x_{i_m} = w_{i_1} w_{i_2} \dots w_{i_m}$$

donde $x_{i_j} \in A$ y $w_{i_j} \in B$ (si elijo el índice $i$ para $x$, elijo el mismo índice $i$ para $w$).

### Caso Soluble:

| $i$ | Lista A ($x_i$) | Lista B ($w_i$) |
| :---: | :---: | :---: |
| **1** | 10 | 1 |
| **2** | 1 | 01 |
| **3** | 00 | 11 |

#### Proceso:
* Comenzamos con el **índice 1**, ya que las cadenas de las listas $A$ y $B$ comienzan con el mismo símbolo (`1`).
* Luego seleccionamos el **índice 2** para compensar los símbolos pendientes.

| Lista / Índice | 1 | 2 | Concatenación resultante |
| :--- | :---: | :---: | :---: |
| **A:** | 10 | 1 | **101** |
| **B:** | 1 | 01 | **101** |

La secuencia de índices que seguimos es **$1 \rightarrow 2$**. Como ambas cadenas son iguales (`101`), esta instancia del PCP **sí tiene solución**.

---

### Caso Insoluble:

Consideremos ahora otro conjunto de cadenas:

| $i$ | Lista A ($x_i$) | Lista B ($w_i$) |
| :---: | :---: | :---: |
| **1** | 10 | 101 |
| **2** | 011 | 11 |
| **3** | 101 | 011 |

#### Intentos de resolución:
* Comenzamos con el **índice 1**, porque los elementos deben coincidir desde el primer símbolo.
* Si intentamos continuar con el **índice 1** o el **índice 2**, aparecen diferencias inmediatas que no se pueden corregir:
  * $1 \rightarrow 1 \implies A: 1010$ vs $B: 101101$
  * $1 \rightarrow 2 \implies A: 10011$ vs $B: 10111$
* Si elegimos el **índice 3**, los símbolos coinciden parcialmente, pero queda un `1` pendiente en la lista $B$:
  * $1 \rightarrow 3 \implies A: 10101$ vs $B: 101011$
* Para intentar compensarlo, volvemos a seleccionar el **índice 3**, pero esto nos lleva nuevamente a la misma situación de desbalance, repitiéndose el proceso indefinidamente sin alcanzar la igualdad entre ambas cadenas.

Esta instancia del PCP **no tiene solución**.

---

## Indecidibilidad del Problema de Correspondencia de Post

El PCP es un **problema indecidible** porque no existe un algoritmo general que, para cualquier par de listas de cadenas, pueda determinar en una cantidad finita de pasos si existe o no una solución.

Si encontramos una secuencia que produce cadenas iguales, podemos comprobar fácilmente que es una solución. Sin embargo, si no encontramos ninguna, no siempre podemos determinar si no existe o si simplemente todavía no la hemos alcanzado.

### Similitud con el Problema de la Parada de Turing (HALT)

El **Problema de la Parada** y el **PCP** son dos problemas fundamentales de indecidibilidad en la teoría de la computación. Además de compartir esta propiedad, existe una relación directa entre ambos mediante una **reducción**:

* La forma en que se demuestra formalmente que el PCP es indecidible es construyendo una reducción desde el Problema de la Parada: si existiera un algoritmo capaz de resolver el PCP en general, ese mismo algoritmo podría usarse para resolver el Problema de la Parada.
* Esto se logra traduciendo cualquier máquina de Turing $M$ y entrada $w$ en una instancia del PCP, de forma que $M$ se detiene con $w$ si y solo si esa instancia del PCP tiene solución.
* Como ya sabemos que el Problema de la Parada es indecidible, si el PCP fuera decidible también lo sería la parada, lo cual es una contradicción. Por lo tanto, el PCP es **indecidible**.

Formalmente, esto se expresa mediante la cadena de reducciones:

$$\text{HALT} \le \text{MPCP} \le \text{PCP}$$

---

## Uso Actual / Importancia en la Teoría

1. **Atajo Matemático para Demostraciones:** Su importancia principal radica en utilizar su indecidibilidad comprobada para medir los límites de otros sistemas modernos. Demostrar que un problema nuevo es indecidible usando la Máquina de Turing directa puede ser muy complejo; el PCP simplifica el proceso mapeando la estructura al "juego de fichas", heredando la indecidibilidad de forma directa.
2. **Límites en Compiladores y Lenguajes de Programación:** El PCP permite definir límites en analizadores sintácticos. Demuestra que es matemáticamente imposible programar un software universal que analice un lenguaje y responda con certeza a preguntas sobre reglas ambiguas o lenguajes distintos que generen exactamente los mismos resultados.
3. **Análisis Heurístico:** Al probar que no puede existir un analizador de código universal e infalible, la industria del software utiliza análisis heurísticos que asumen un margen de error, o diseña lenguajes más restrictivos de base.
4. **Álgebra y Geometría:** En la actualidad, el PCP se utiliza para demostrar que ciertos problemas geométricos o de álgebra lineal no tienen solución (por ejemplo, el problema de la mortalidad de matrices o el problema de teselación/baldosado del plano infinito).
