[GitDiagram](https://gitdiagram.com/L-u-c-i-a-M/tp-funciones)
- [Gitingest](https://gitingest.com/https://github.com/L-u-c-i-a-M/tp-funciones?utm_source=chatgpt.com)
- [RepoGrep](https://repogrep.com/L-u-c-i-a-M/tp-funciones)
- [DeepWiki](https://deepwiki.com/L-u-c-i-a-M/tp-funciones)
- [GitHub1s](https://github1s.com/L-u-c-i-a-M/tp-funciones/tree/main)

# TP Funciones - Python

## Descripción

Este proyecto es un trabajo práctico educativo que demuestra los conceptos fundamentales de funciones en Python a través de 5 ejercicios progresivos. Cada ejercicio ilustra diferentes características del lenguaje: funciones nombradas vs anónimas (lambda), argumentos posicionales y por palabra clave, parámetros por defecto, parámetros opcionales y manejo básico de errores. Está destinado a estudiantes que aprenden programación en Python y sirve como referencia práctica de la sintaxis y uso de funciones.

## Tecnologías utilizadas

- **Python 3.x**: Lenguaje principal utilizado para implementar todos los ejercicios. Se aprovechan características como funciones de primera clase, lambdas, argumentos con palabras clave obligatorias (*), parámetros por defecto y manejo de excepciones.

## Características principales

- Demostración de funciones nombradas (def) vs funciones anónimas (lambda)
- Uso de argumentos posicionales y argumentos por palabra clave obligatorios (keyword-only)
- Parámetros con valores por defecto
- Parámetros opcionales usando None como valor centinela
- Manejo básico de errores con raise ValueError
- Ejemplos de cálculo matemático: suma, resta, precio con IVA, conversión de unidades, área de figuras

## Arquitectura del proyecto

El proyecto consta de 5 módulos independientes (ejercicio1.py a ejercicio5.py), cada uno enfocado en un concepto específico de funciones. No hay dependencias entre módulos; cada archivo se ejecuta de forma autónoma e imprime sus resultados en consola.

```
tp-funciones/
├── ejercicio1.py   # Funciones básicas: suma (nombrada y lambda)
├── ejercicio2.py   # Argumentos keyword-only en función nombrada
├── ejercicio3.py   # Parámetros por defecto (IVA 21%)
├── ejercicio4.py   # Parámetros por defecto + validación (conversión unidades)
└── ejercicio5.py   # Parámetros opcionales con None (área rectángulo/cuadrado)
```

## Estructura de carpetas y archivos

```
tp-funciones/
├── ejercicio1.py   # Funciones suma: nombrada y lambda
├── ejercicio2.py   # Funciones resta: keyword-only args
├── ejercicio3.py   # Funciones precio final: parámetros por defecto
├── ejercicio4.py   # Funciones conversión: validación + default
├── ejercicio5.py   # Funciones área: parámetro opcional con None
└── README.md       # Este archivo
```

## Requisitos previos

- Python 3.6 o superior
- Terminal / línea de comandos

## Instalación

1. Clonar o descargar el repositorio:
   ```bash
   git clone <url-del-repositorio>
   ```
2. Ingresar a la carpeta del proyecto:
   ```bash
   cd tp-funciones
   ```
3. No se requieren dependencias adicionales (solo librería estándar de Python)

## Configuración

No se requiere configuración adicional. El proyecto no utiliza variables de entorno, archivos de configuración, bases de datos ni servicios externos.

## Ejecución

Ejecutar cada ejercicio individualmente desde la terminal:

```bash
python ejercicio1.py
python ejercicio2.py
python ejercicio3.py
python ejercicio4.py
python ejercicio5.py
```

Cada script imprime directamente sus resultados en la consola.

## Funcionamiento general

1. El usuario abre una terminal en la carpeta del proyecto
2. Ejecuta el archivo Python deseado (ejercicio1.py a ejercicio5.py)
3. El script define las funciones (nombradas y/o lambda)
4. Llama a las funciones con valores de prueba
5. Imprime los resultados en consola
6. El programa termina

## Comunicación entre componentes

No hay comunicación entre componentes. Cada ejercicio es un script independiente que se ejecuta de forma aislada. La única "comunicación" es la salida estándar (stdout) hacia la consola.

## Eventos, rutas o endpoints

No aplica. No es una aplicación web, API ni sistema basado en eventos. Son scripts de consola que se ejecutan directamente.

## Comunicación Frontend → Backend

No aplica. No hay frontend ni backend.

## Comunicación Backend → Frontend

No aplica. No hay frontend ni backend.

## Funciones o mecanismos importantes

### ejercicio1.py - Funciones básicas
- `suma_nombrada(num1, num2)`: Función tradicional con `def` que retorna la suma
- `suma_anonima = lambda num1, num2: num1 + num2`: Función lambda equivalente
- **Concepto**: Las lambdas son funciones anónimas de una sola expresión, útiles para operaciones simples

### ejercicio2.py - Argumentos keyword-only
- `resta_nombrada(*, num1, num2)`: El `*` obliga a llamar a la función usando palabras clave: `resta_nombrada(num1=10, num2=3)`
- **Concepto**: Los argumentos después de `*` son keyword-only, mejoran legibilidad y evitan errores de orden

### ejercicio3.py - Parámetros por defecto
- `precio_final_nombrada(precio, iva=0.21)`: El IVA tiene valor por defecto 21%
- Permite llamar `precio_final_nombrada(100)` (usa 21%) o `precio_final_nombrada(100, iva=0.10)` (usa 10%)
- **Concepto**: Parámetros opcionales con valores por defecto al final de la firma

### ejercicio4.py - Validación + parámetros por defecto
- `convertir_nombrada(metros, unidad="cm")`: Convierte metros a cm (default) o mm
- Lanza `ValueError` si la unidad no es soportada
- Lambda equivalente con expresión condicional ternaria
- **Concepto**: Validación de entrada + parámetros por defecto + manejo de errores

### ejercicio5.py - Parámetros opcionales con None
- `area_nombrada(base, altura=None)`: Si `altura` es None, calcula área de cuadrado (base × base); si se proporciona, calcula rectángulo (base × altura)
- **Concepto**: Usar `None` como valor centinela para detectar si se pasó el argumento opcional

## Identificación y gestión de usuarios

No aplica. El proyecto no maneja usuarios, autenticación ni sesiones.

## Errores, estados y desconexiones

- **ejercicio4.py**: Lanza `ValueError("Unidad no soportada. Usar 'cm' o 'mm'.")` si se pasa una unidad inválida
- No hay manejo de excepciones en los otros ejercicios (son ejemplos básicos)
- No hay conexiones de red, bases de datos ni estados persistentes que gestionar

## Capturas de pantalla

Ejemplo de salida de `python ejercicio1.py`:
```
Resultado 1: 15
Resultado 2: 10
```

Ejemplo de salida de `python ejercicio2.py`:
```
Resta nombrada (10 - 3): 7
Resta anónima (10 - 3): 7
```

Ejemplo de salida de `python ejercicio3.py`:
```
Precio final nombrado (100, IVA 21%): 121.0
Precio final anónimo (100, IVA 21%): 121.0
Precio final nombrado (100, IVA 10%): 110.0
Precio final anónimo (100, IVA 10%): 110.0
```

Ejemplo de salida de `python ejercicio4.py`:
```
1 metro a cm (nombrado): 100
1 metro a mm (nombrado): 1000
1 metro a cm (anónimo): 100
1 metro a mm (anónimo): 1000
```

Ejemplo de salida de `python ejercicio5.py`:
```
Área rectángulo nombrado (base=5, altura=3): 15
Área cuadrado nombrado (base=5): 25
Área rectángulo anónimo (base=5, altura=3): 15
Área cuadrado anónimo (base=5): 25
```

## Pruebas realizadas

| Prueba | Acción realizada | Resultado esperado | Resultado obtenido |
|--------|------------------|-------------------|-------------------|
| Ejercicio 1 | Ejecutar `python ejercicio1.py` | Suma 5+10=15 y 7+3=10 | OK |
| Ejercicio 2 | Ejecutar `python ejercicio2.py` | Resta 10-3=7 en ambas funciones | OK |
| Ejercicio 3 | Ejecutar `python ejercicio3.py` | Precio 100 con IVA 21% = 121, IVA 10% = 110 | OK |
| Ejercicio 4 | Ejecutar `python ejercicio4.py` | 1m = 100cm, 1m = 1000mm | OK |
| Ejercicio 5 | Ejecutar `python ejercicio5.py` | Rectángulo 5×3=15, Cuadrado 5×5=25 | OK |
| Ejercicio 4 - Error | Llamar `convertir_nombrada(1, "km")` | ValueError con mensaje claro | OK |

## Problemas conocidos

- No hay manejo de errores para tipos de datos incorrectos (ej. pasar strings en lugar de números)
- No hay tests automatizados (pytest/unittest)
- Los ejercicios son independientes y no reutilizan código común
- No hay documentación en formato docstring en las funciones

## Mejoras futuras

- Agregar docstrings a todas las funciones siguiendo convenciones (PEP 257)
- Implementar tests unitarios con pytest
- Agregar type hints (type annotations) para mejor documentación estática
- Crear un script principal que ejecute todos los ejercicios secuencialmente
- Incluir ejercicios adicionales: *args, **kwargs, closures, decoradores
- Manejar excepciones de tipo (TypeError) en validaciones de entrada

## Autores y responsabilidades

| Integrante | Responsabilidad |
|------------|-----------------|
| Lucía M. | Desarrollo completo de los 5 ejercicios y documentación |

## Repositorio

El código fuente se encuentra disponible en: https://github.com/L-u-ci-a-M/tp-funciones

## Licencia

Este proyecto fue desarrollado con fines educativos.

## Conclusión

Este trabajo práctico permitió afianzar los conceptos fundamentales de funciones en Python: la sintaxis de funciones nombradas vs lambdas, el uso de argumentos posicionales y keyword-only, parámetros por defecto, parámetros opcionales con centinelas None, y validación básica con excepciones. Las dificultades principales surgieron al comprender cuándo usar lambdas vs funciones nombradas (las lambdas son limitadas a una expresión) y el patrón de `None` como valor centinela para distinguir "no pasado" de "pasado explícitamente como None". Estos conceptos son reutilizables en cualquier proyecto Python que requiera APIs limpias y flexibles.